# 001-reidmamba 实验现状 / AI 接手入口

> **本文件是后续 AI/人接手 001-reidmamba 消融实验的单一入口（human-readable 全景 + 事件/决策记录）。**
> **运行态结构化 SSOT = `Exp/registry.yaml`**；实时进程态 = `monitor light`（`python3 .claude/skills/ofr_cli.py monitor light`）。
> 最后更新：2026-06-26 21:05 (CH-1) ｜ 方法 MGFROFR ｜ baseline MambaOFR

## ⚠️ 当前论文叙事方向（2026-06-26，最高优先，新对话必读）

**主线已切换：`F1`(MGFE+RATR, avg fusion) = main model；A3(max fusion) 降为 fusion 消融对照。**

- **起因（D2 判定）**：原 full=A3 负协同失败——全参考 A3(27.17) < A1(27.75)/A2(27.72)/F1(27.86)。
- **决策 SSOT**：`Paper/writing/review/round1/d2-decision-record-20260626.md`（完整数据 + N1 硬门 + 5-Phase 方案 + 决策 N1–N5）。
- **数字未冻结**：N1 数据可比硬门未过——(a) checkpoint 口径不统一（A3=net_g_65000 / F1=net_g_best）；(b) A0 对比误用旧 placeholder 25.99，应用 baseline_floor Y 26.84。冻结前 F1/A3 任何数字不得进论文/letter。
- **RATR 定位**：可解释多样性正则（l_ratr=-0.057），非 PSNR 性能模块。
- 下方「30 秒速览 / 训练分布」为 06-24 RATR 修复事件记录，仍有效但非最新叙事方向。

## 0. 30 秒速览
- project-internal 统一重训协议：A0–A3 + 设计消融，同 pipeline / 同 200k budget / 统一 warm-start 自 `baselines/trained/mambaofr_reds_16/models/net_g_best.pth`。
- **当前主线事件**：RATR loss 时间中心化 bug 修复（commit `d072672f`，知识库 `know-092`）。b1/t1 因 RATR 失效已用修复后 loss 重训。
- 三机：A100×4 + 4090×(2+2) 可触达；L40×4 **SSH 暂不可达**（进程仍在跑）。

## 1. 当前训练分布与进度（截至 2026-06-24 12:50，monitor light）
全部 `total_iter=200000`。A100/4090 跑**旧 loss**（修复前），仅 b1/t1 跑**修复后 loss**。

| 变体 | 角色 | server/GPU | iter | loss 版本 | 状态 | ETA(到200k) |
|---|---|---|---|---|---|---|
| A1 | +MGFE(无RATR) | a100/0 | 155500 | 旧(不受影响) | running | ~22.5h → 06-25 上午 |
| A2 | +RATR(健康0.9x) | a100/1 | 150600 | 旧(不重训) | running | ~26.5h → 06-25 下午 |
| A3 | full(健康1.2x) | a100/2 | 150900 | 旧(不重训) | running | ~26h → 06-25 下午 |
| M1 | RATRPearson | a100/3 | 141300 | 旧(不受影响) | running | ~31h → 06-25 晚 |
| F1 | fusion avg(健康1.1x) | 4090_0/0 | 125000 | 旧(可暂留) | running | ~37h → 06-26 凌晨 |
| B1 | branches=4(塌缩22.4x) | 4090_0/1 | ~100 | **修复后** | **重训中** | 从0约4.5–5天 → 06-28/29 |
| T1 | tokens=24(塌缩15.1x) | 4090_1/0 | ~100 | **修复后** | **重训中** | 从0约4.5–5天 → 06-28/29 |
| D1 | diversity(正交) | 4090_1/1 | 127200 | 旧(不受影响) | running | ~36h → 06-26 凌晨 |
| G2 | 8t/2b | l40/0 | — | 旧 | running(SSH不可达) | 待确认 |
| G4 | 16t/4b(高危) | l40/1 | — | 旧 | running(SSH不可达) | 待确认 |
| G1 | 4t/1b(G=1无效) | l40/2 | — | 旧 | running(SSH不可达) | — |
| R1 | tau=0.05 | l40/3 | — | 旧 | running(SSH不可达) | 待确认 |

> A0 baseline 已完成（best 28.48 @175k，L40，见 registry `best_metrics`）。

## 2. RATR 时间中心化修复事件
**根因**：MGFE branch descriptor 被帧不变常数主导（`const:fluct ratio = descr_abs_mean / cross_frame_std`，随 token×branch 增大而升高）→ `F.normalize` 后各帧方向趋同 → cross-frame 相似度行变平 → soft Kendall-tau 塌缩 → `l_ratr≈0`。

**修复**（`losses/ratr_loss.py:92-100`）：`F.normalize` 前减 per-(video,branch,channel) 时间均值，让 ranking 作用于帧变化分量。TDD 红绿 + 22 tests passed。

**塌缩规律**（真实 checkpoint 诊断，6 变体）：token×branch **> 12t/3b 基准 → 塌缩失效**；**≤ 基准 → 健康**。

| 变体 | 几何 const:fluct | l_ratr 修复前 | 修复后 | 结论 |
|---|---|---|---|---|
| b1(12t/4b) | 22.4x | ≈0 (+3e-6) | +0.062 | **塌缩→RECOVERED** |
| t1(24t/3b) | 15.1x | ≈0 (-7e-8) | +0.043 | **塌缩→RECOVERED** |
| a3(12t/3b) | 1.2x | -0.057 | -0.024 | 健康(信号保留) |
| f1(12t/3b) | 1.1x | -0.057 | -0.049 | 健康 |
| a2(RATR only) | 0.9x | -0.057 | -0.052 | 健康 |
| d1(diversity) | cos 0.004 正交 | — | ≈4e-6 | 健康(误报，非失效) |

**effective RATR weight = 0.1**：yml `ratr_loss_weight: 1.0` × `RATRLoss.loss_weight=0.1` 默认（`ratr_loss.py:19`）。早前 0.01 记述有误。

指针：`memory/knowledge/know-092-ratr-time-centering-fix.md`；commit `d072672f`；测试 `tests/test_ratr_loss_time_centering.py`；诊断脚本 `Exp/scripts/diagnose_ratr_signal.py`（须 GPU）；workflow bundle `docs/workflow/10-active/20260624-123500-ratr-time-centering-diagnosis/`。

## 3. 重训决策（防止后来 AI 误判，2026-06-24 蔡博拍板）
- **已重训** b1、t1：旧失效 checkpoint 归档 `experiments/mgfrofr_{b1_4b,t1_24t}_archived_ratrbuggy_20260624`，修复后 loss 从 iter0 重训。**iter5000 验证门**：判 `|l_ratr|>0.01`（预期 b1 +0.062 / t1 +0.043）通过后放长 200k。
- **不重训** a2、a3（时间约束）：
  - a2 零风险（对照“有无 RATR”，与 branch/token 几何无关）。
  - a3 唯一纸面瑕疵（b1/t1 修复后 vs a3 修复前混入 loss 实现差异），但 a3 RATR 本健康、effective weight 0.1，主指标影响有限，结论预期不翻转。
  - **兜底**：测试比主指标(PSNR/SSIM/Rank-1)非 l_ratr；论文 a3 处加一句健康声明。
- **待确认**（L40 恢复后诊断）：g4(16t/4b 高危疑塌缩)、g2(8t/2b)。
- **排除**：g1(G=1 RATR 无作用)、m1(Pearson)、d1(diversity)、a0/a1(无 RATR)。

## 4. b1/t1 vs a3 配置公平性（yml diff 核对，CH-1）
逐行核对 `mgfrofr_{a3,b1,t1}.yml`（均 138 行）：仅 **branch/token 设计变量**（b1 `mgfe_num_branches` 3→4；t1 `mgfe_num_tokens` 12→24）+ **无害机制差异**（`use_checkpoint` a3=false / b1,t1=true 数值等价；`resume_state` a3 续训 / b1,t1 全新，同 baseline 同 200k）+ `ratr_loss.py` 修复，**无超参漂移**。`total_iter / lr / scheduler / loss 权重 / 数据集 / seed` 全一致。

## 5. 关键指针 / SSOT
- **运行态 SSOT**：`Exp/registry.yaml`（variants + runs + best_metrics + use_checkpoint_policy）。
- **实时进程**：`python3 .claude/skills/ofr_cli.py monitor light`。
- **修复知识**：`memory/knowledge/know-092-ratr-time-centering-fix.md`。
- **workflow bundle**：`docs/workflow/10-active/20260624-123500-ratr-time-centering-diagnosis/`。
- `Exp/ablation_journal.md`：**2026-03 首轮 L40 历史记录（registry 标 `lost_data`），仅供参考、不得用于论文/rebuttal 引用**。
- baseline floor（A0，30 clips）：Y-PSNR 26.84 / SSIM 0.9153，见 registry `best_metrics.baseline_floor`。

## 6. 下一步待办
1. b1/t1 到 iter5000 复测验证门（约 2–3h 内）。
2. L40 恢复后：诊断 g4/g2 是否塌缩，定是否重训。
3. b1/t1 重训完成（~06-28/29）后，与 a3 比主指标完成 MGFE 粒度消融。
