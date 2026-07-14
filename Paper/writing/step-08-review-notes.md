# Step 8: Review 汇总

> 聚合 Round 2/3 审查结论 + 投稿前审查 + 图表专项审查

## P0 阻断

### P0-1: Metric Provenance Conflict (mdpi-pre-submission-blockers.md)
论文 Table 1 MambaOFR PSNR `25.99` vs baseline log `24.9938` (差1.00dB)
MgfrOFR SSIM/DISTS `0.9237/0.0653` vs A3 log `0.9137/0.0803`
retrained A0 (27.39) > A3 (27.13) — 直接用内部数据则消融叙事负面

**需决策**: 协议A(external pretrained) or 协议B(internal retrained)

### P0-2: 图表超量 (figures_review.md)
12 Figures + 10 Tables = 22 items, MDPI标准10-14
已有压缩方案待执行

## P1 (审稿人可能质疑)

### 技术类
- FIG-P1-1: Fig2 "Eq.(12)" 引用错位 — 实际对应recalibration
- FIG-P1-2: Fig8 caption "(dashed)" 与图体不符
- RATR超参sensitivity分析缺失 (仅MGFE有)
- 单benchmark (SRWOV) 无跨数据集验证
- Real-world improvement CLIP-IQA+ +0.006 统计显著性边界

### 图表类
- Fig6 real-world 缺红色框zoom-in
- Caption动词: 多处 shows/presents → 应改为 illustrates/demonstrates
- Table压缩: 10→5-6 (合并sensitivity tables, 删module_summary/feature_comparison)

### 写作类
- 无Teaser figure (nice-to-have)
- 无Failure case analysis
- Abstract需根据最终数据更新

## P2 (润色)
- Conclusion 精简重复内容
- 交叉引用全面验证
- benchmarks.yaml ranking text 一致性 (infra)
