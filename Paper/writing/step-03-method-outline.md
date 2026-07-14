# Step 3: Method 写作思路 + 训练启动

## Method 结构
- 3.1 Overview: MambaOFR backbone + MGFE/RATR 挂载点
- 3.2 MGFE: progressive max fusion → token insertion → branch-specific mixer → recalibration
- 3.3 RATR: differentiable Kendall's Tau on temporal correspondences
- 3.4 Compared with Closest Prior Work (ReIDMamba)
- 3.5 Loss Function (L_pix + L_perc + L_gan + λ_ratr·L_ratr)

## 消融训练
| Setting | 目录 | 启用 | 迭代 |
|---------|------|------|------|
| A0 | mgfrofr_a0_baseline | baseline only | 200K |
| A1 | mgfrofr_a1_mgfe | +MGFE, -RATR | 200K |
| A2 | mgfrofr_a2_ratr | -MGFE recalib, +RATR | 200K |
| A3 | mgfrofr_a3_full | MGFE + RATR | 200K |

## 关键修改 (Round 3)
- tau符号消歧: frame-index tau→t, DKTau tau保留
- Algorithm 1: RATR移出for t循环, clip-level执行
- Eq.22: 0.1系数引用FiLM conservative residual scaling
- token fusion标注 "adapted from ReIDMamba"
