# 001-reidmamba / A3 Full 训练异常分析

- 生成时间：`2026-03-23T23:22:32+08:00`
- 影响范围：`projects/001-reidmamba/Exp/experiments/mgfrofr_a3_full/`

## 已验证事实（结论先行）

1. `tmux` 中不存在 `reidmamba_a3` session（A0/A1/A2 仍在）。
2. `nvidia-smi` 显示 GPU3 空闲（util 0%、显存 0 MiB），A3 训练进程已退出/被杀，不是“还在跑但没打印”。
3. A3 训练日志 `projects/001-reidmamba/Exp/experiments/mgfrofr_a3_full/train_mgfrofr_a3_full_20260322_235554.log:1342`～`projects/001-reidmamba/Exp/experiments/mgfrofr_a3_full/train_mgfrofr_a3_full_20260322_235554.log:1343` 停在 `iter=30000` 的保存阶段（“Saving models and training states.”），文件 `mtime=2026-03-23 23:01:08 +0800`；并且 30000 后无验证输出（上一条 `Validation OldFilmval` 在 `projects/001-reidmamba/Exp/experiments/mgfrofr_a3_full/train_mgfrofr_a3_full_20260322_235554.log:1289`）。
4. `projects/001-reidmamba/Exp/experiments/mgfrofr_a3_full/training_states/30000.state` 文件已损坏：`torch.load()` 报 `failed finding central directory`；而 `25000.state` 可正常加载。
5. A0/A1/A2 的 `training_states/30000.state` 均可正常加载，说明不是“所有实验统一保存坏了”。
6. 保存与验证的顺序是“先保存再验证”（`framework/basicsr/train.py:205`～`framework/basicsr/train.py:216`），结合第 3 点可定位：中断发生在 `model.save()`（保存权重/训练状态）内部或其附近。

**结论**：A3 在保存 `30000.state` 的过程中被中断（SIGKILL/SIGTERM/掉电/崩溃等），留下损坏 state；随后进程退出，`tmux` session 消失，GPU3 释放。

## 证据（可复现命令）

### 1) tmux session 缺失

```bash
tmux ls
```

观察：输出包含 `reidmamba_a0`/`reidmamba_a1`/`reidmamba_a2`，不包含 `reidmamba_a3`。

### 2) GPU3 空闲

```bash
nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv,noheader
```

关键行：

```
3, NVIDIA L40, 0 %, 0 MiB, 46068 MiB
```

### 3) 日志停在保存点

```bash
tail -n 2 projects/001-reidmamba/Exp/experiments/mgfrofr_a3_full/train_mgfrofr_a3_full_20260322_235554.log
```

关键尾部：

```
2026-03-23 23:01:08,533 INFO: [mgfro..][epoch:  1, iter:  30,000, lr:(2.000e-04,)] ...
2026-03-23 23:01:08,544 INFO: Saving models and training states.
```

### 4) `30000.state` 已损坏（能直接触发）

```bash
python3 - <<'PY'
import torch
print(torch.load('projects/001-reidmamba/Exp/experiments/mgfrofr_a3_full/training_states/25000.state', map_location='cpu').get('iter'))
torch.load('projects/001-reidmamba/Exp/experiments/mgfrofr_a3_full/training_states/30000.state', map_location='cpu')
PY
```

报错（关键信息）：

```
PytorchStreamReader failed reading zip archive: failed finding central directory
```

> 备注：`projects/001-reidmamba/Exp/experiments/mgfrofr_a3_full/models/net_g_30000.pth`/`net_d_30000.pth` 可正常 `torch.load()`；损坏点集中在 `training_states/30000.state`（优化器/调度器状态）。

## 可能原因（需要额外证据才能定责）

按概率排序：

1. **外部 SIGKILL/SIGTERM** 在写 `.state` 期间打断（人工 kill、守护脚本、作业系统 walltime、OOM killer 等）。
   - 这类中断通常不会给 `train_*.log` 写 traceback（traceback 走 stderr/tmux pane），最终只留下“半写文件 + 进程退出”。
2. **瞬时 I/O 异常**（例如短暂的 `EIO`）导致进程异常退出/被上层终止，同样可能留下不完整的 zip。
3. **进程崩溃但异常未进入 logger**：PyTorch 序列化/底层库触发致命异常，stdout 日志停在保存前一行，stderr 在 tmux pane 中可见但不会写入 `train_*.log`。

当前不足以分辨 1/2/3：本机 `dmesg` 无权限（`dmesg: 读取内核缓冲区失败: 不允许的操作`）；`journalctl -k --since '2026-03-23 23:00:00' --until '2026-03-23 23:03:00'` 返回 `-- No entries --`，未直接看到 OOM/驱动级别报错；训练日志也没有 traceback。

## 修复建议

### A) 立刻恢复训练（最保守、最可复现）

目标：从最后一个**完整**的训练状态继续（`25000.state`）。

1. **保护现场**：先把坏文件改名，避免 `--auto_resume` 误选它，同时保留取证。
   - `mv projects/001-reidmamba/Exp/experiments/mgfrofr_a3_full/training_states/30000.state projects/001-reidmamba/Exp/experiments/mgfrofr_a3_full/training_states/30000.state.corrupt`
2. **重新启动 A3**（同一 YAML）并使用自动恢复：
   - `python framework/train.py -opt projects/001-reidmamba/Exp/options/train/mgfrofr_a3.yml --auto_resume`
3. **启动后自检**：
   - 新日志应出现 `Resuming training ... iter: 25000`（或更早但不应是 30000）。
   - `nvidia-smi` 应看到 GPU3 重新占用并有 python 进程。

### B) 真的要“从 30000 继续”（不推荐）

只能做“权重级恢复”：加载 `models/net_g_30000.pth`/`net_d_30000.pth` 作为预训练，但**优化器/调度器状态丢失**，训练轨迹会改变，结果不可与原 run 严格对齐。

## 防复发（最小改动方向）

1. **原子写入训练状态**：把 `torch.save(state, save_path)` 改成 “写临时文件 + `os.replace()`”，避免留下损坏的“最新 state”。
   - 位置：`framework/basicsr/models/base_model.py:344`～`framework/basicsr/models/base_model.py:375`（当前直接写目标文件）。
2. **把异常栈落盘**：在 `framework/basicsr/train.py` 的保存/验证段外围加 `try/except` + `logger.exception(...)`，保证 traceback 进入 `train_*.log`，避免再次“只剩一行 Saving...”。
3. **外部 kill 定责**：如果确认是作业系统/守护脚本干预，给 checkpoint 窗口留“不可杀”白名单或调整 walltime/策略；否则同类中断会重复发生。

## 定责所需的额外检查（你补充执行）

- 内核/系统日志（若可访问）：
  - `journalctl -k --since '2026-03-23 22:55:00' --until '2026-03-23 23:10:00' | rg -i 'killed process|oom|xid|nvrm|gpu'`
  - 若有权限：`dmesg -T | rg -i 'killed process|oom|xid|nvrm|gpu'`
- 若有作业系统（Slurm/容器平台等）：检查 A3 对应任务是否在 `2026-03-23 23:01` 左右被系统终止（walltime/抢占/节点维护）。
