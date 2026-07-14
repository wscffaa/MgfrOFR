# Step 2: Story + Introduction 写作思路

## 4段式故事线
1. 任务: 老电影修复，SRWOV benchmark
2. 局限: 现有方法单流隐空间瓶颈，缺乏多粒度特征表达
3. 方法: MGFE (multi-granularity feature extraction) + RATR (ranking-aware triplet regularization)
4. 贡献 (4条):
   - Adapt MGFE from ReIDMamba, extend with channel-wise recalibration
   - Propose RATR for branch diversity enforcement
   - Achieve 27.13dB PSNR (+1.14dB over MambaOFR)
   - NIQE 5.06, BRISQUE 18.70 on real-world

## 实验清单
- Comparison: SRWOV synthetic (30 clips) + real-world (216 clips), vs 10 baselines
- Ablation: A0(baseline)/A1(+MGFE)/A2(+RATR)/A3(full) + G1/G2 granularity variants
- Metrics: PSNR/SSIM/LPIPS/DISTS (synthetic), NIQE/BRISQUE/CLIP-IQA+ (real)

## 关键决策
- 贡献声明从 "We design" 改为 "We adapt ... and extend with"
- Pipeline 图放在 Introduction 末尾
- 末段追加具体数字 teaser (27.13 dB PSNR, +1.14 dB)
