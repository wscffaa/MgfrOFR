# MGFROFR 论文修改记录

## Round 2 (2026-04-14)
### 修改内容
- Introduction: 贡献声明 "We design" → "We adapt ... and extend with"
- Method: token fusion标注 "adapted from ReIDMamba", max/mean fusion引用依据
- Related Work: Table 1周围冗余叙述精简
- Results: 定性图选帧标准(PSNR>=26+Delta>=0.5), Complexity Table硬件标注
- Discussion: branch similarity统计范围明确 (3,000 frames from 30 clips)
- Conclusion: 精简重复Limitations段
### Review 发现
- M1: 贡献声明需如实描述 → 已修复
- M2: Setting B训练过程分析 → 后续W2完成
- M3: per-clip统计显著性 → 后续W1完成
### 仍未解决
- 图表V1-V4全部失败, 进入V5数据驱动选帧

## Round 3 (2026-04-17 ~ 2026-04-19)
### 修改内容
- Method: tau符号消歧(frame→t), Algorithm 1 RATR clip-level, Eq.22 FiLM引用
- Introduction: 语气收敛ApplSci, 贡献列表精简, 删Notation表
- Conclusion: ABC三段→五段, 新增Application Impact+Future Work 4条
- Abstract: 187词, MDPI 4段式 (问题/方法/结果/影响)
- 12图全部vector PDF: Fig1 PIL像素修复, Fig4字体, Fig5字号+bbox, Fig6 aspect
- Related Work: 期刊比例35.5%→50.6%, 15条新增, 5条TODO修复
- Table 9: 三baseline复杂度实测, Speed s/iter→ms/frame
### Review 发现
- Wilcoxon: PSNR p=3.7e-09***, SSIM p=3.5e-03**, LPIPS/DISTS n.s.
- Train-test inversion: B training L_perc最低→test LPIPS最差(+75%)
- 诚实性决策: "p<0.001 for all"改为如实报告各指标
- FIG-P1-1: Fig2 Eq引用错位
- FIG-P1-2: Fig8 caption不符
### 仍未解决
- P0 metric provenance conflict (协议A vs B需决策)
- 图表22→10-14压缩待执行
- Fig6 zoom-in缺失
- Caption动词审计

## Round 5 (2026-05-10)
### 修改内容
- 同步 GPT5.4 Pro 修订投稿包到 `Paper/applsci`：主 TeX、authors、Introduction、Related Work、Method、Results、Discussion、Conclusion。
- 新增 `applsci/submission_extras/cover_letter/Cover_Letter_MgfrOFR_Revised.tex` 与 `applsci/submission_extras/supplementary/Supplementary_Protocol_MgfrOFR.tex`。
- 同步 revised 投稿资产到 `Paper/submission_applsci`，使用 revised 路径保留旧 PDF/ZIP。
- 保留项目内已有 Qi Zhang ORCID 和 `figure_manifest.yaml` 图表治理元数据。

### Review 发现
- GPT5.4 Pro 修复包覆盖 8 类问题：创新性聚焦、RATR 边界定义、复杂度口径、证据强度收敛、supplementary 自洽、Data Availability、Human-evaluation threat、Cover Letter。
- 修订版仍使用 `27.13 / 0.9237 / 0.0653` 等敏感指标值，必须继续受 P0 metric provenance gate 约束。

### 仍未解决
- 提交前需要新鲜验证：源码结构比对、LaTeX 编译、投稿资产检查、MDPI Mode C 快速门禁。
