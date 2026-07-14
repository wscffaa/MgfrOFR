#!/bin/bash
# 001-reidmamba 训练完成自动测试脚本
# 监控 a1/a2/a3 训练进度，完成后自动启动 tmux 测试
# 用法: nohup bash auto_test_on_complete.sh &

set -euo pipefail

RTN_PYTHON="${HOME}/miniconda3/envs/rtn/bin/python"
OFR_ROOT=/mnt/data/Antigravity_OFR
FRAMEWORK=$OFR_ROOT/framework
OPT_DIR=$OFR_ROOT/projects/001-reidmamba/Exp/options/test
EXP_DIR=$OFR_ROOT/projects/001-reidmamba/Exp/experiments
TARGET_ITER=200000
POLL_INTERVAL=120  # 每 2 分钟检查一次

# 实验映射: index -> (exp_name, gpu_id, tmux_session)
declare -A EXP_NAMES=( [1]="mgfrofr_a1_mgfe" [2]="mgfrofr_a2_ratr" [3]="mgfrofr_a3_full" )
declare -A GPU_IDS=( [1]=1 [2]=2 [3]=3 )
declare -A LAUNCHED=( [1]=1 [2]=1 [3]=0 )  # a1/a2 已手动启动，只监控 a3
WAIT_AFTER_COMPLETE=60  # 等待 checkpoint 写盘

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

get_iter() {
    local exp_name=$1
    local log_file
    log_file=$(find "$EXP_DIR/$exp_name" -name "train_${exp_name}_*.log" 2>/dev/null | sort | tail -1)
    if [ -z "$log_file" ]; then
        # fallback: any log that's not opt.log
        log_file=$(find "$EXP_DIR/$exp_name" -name "*.log" ! -name "opt.log" 2>/dev/null | sort | tail -1)
    fi
    if [ -n "$log_file" ]; then
        grep -oP 'iter:\s*\K[\d,]+' "$log_file" 2>/dev/null | tail -1 | tr -d ','
    else
        echo "0"
    fi
}

launch_test() {
    local idx=$1
    local exp_name=${EXP_NAMES[$idx]}
    local gpu=${GPU_IDS[$idx]}
    local session="reid_test_a${idx}"
    local syn_opt="$OPT_DIR/mgfrofr_a${idx}_synthetic.yml"
    local real_opt="$OPT_DIR/mgfrofr_a${idx}_realworld.yml"
    local syn_log="/tmp/reid_a${idx}_syn.log"
    local real_log="/tmp/reid_a${idx}_real.log"

    log "🚀 Launching test for $exp_name on GPU $gpu (tmux: $session)"

    tmux new-session -d -s "$session" \
        "cd $FRAMEWORK && \
        CUDA_VISIBLE_DEVICES=$gpu $RTN_PYTHON test.py -opt $syn_opt 2>&1 | tee $syn_log && \
        CUDA_VISIBLE_DEVICES=$gpu $RTN_PYTHON test.py -opt $real_opt 2>&1 | tee $real_log; \
        echo DONE > /tmp/reid_a${idx}_done.flag; exec bash"

    log "✅ $session started: synthetic → realworld on GPU $gpu"
}

# ─── 主循环 ───
log "========================================="
log "001-reidmamba 自动测试监控启动"
log "监控目标: a1(GPU1) a2(GPU2) a3(GPU3)"
log "目标迭代: ${TARGET_ITER}"
log "轮询间隔: ${POLL_INTERVAL}s"
log "========================================="

all_done=0
while [ $all_done -eq 0 ]; do
    all_done=1
    for idx in 1 2 3; do
        # 已启动的跳过
        if [ ${LAUNCHED[$idx]} -eq 1 ]; then
            continue
        fi

        exp_name=${EXP_NAMES[$idx]}
        current_iter=$(get_iter "$exp_name")
        current_iter=${current_iter:-0}

        if [ "$current_iter" -ge "$TARGET_ITER" ]; then
            log "✅ $exp_name 训练完成 (iter=$current_iter >= $TARGET_ITER)"
            log "⏳ 等待 ${WAIT_AFTER_COMPLETE}s 确保 checkpoint 写盘..."
            sleep $WAIT_AFTER_COMPLETE
            # 确认 net_g_latest.pth 存在
            ckpt="$EXP_DIR/$exp_name/models/net_g_latest.pth"
            if [ ! -f "$ckpt" ]; then
                log "⚠️ $ckpt 未找到，再等 60s..."
                sleep 60
            fi
            launch_test "$idx"
            LAUNCHED[$idx]=1
        else
            all_done=0
            log "⏳ $exp_name: iter=$current_iter/$TARGET_ITER"
        fi
    done

    if [ $all_done -eq 0 ]; then
        sleep $POLL_INTERVAL
    fi
done

log "========================================="
log "🎉 所有训练完成，全部测试已启动！"
log "tmux sessions: reid_test_a1, reid_test_a2, reid_test_a3"
log "========================================="
