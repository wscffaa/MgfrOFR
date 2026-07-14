# Step 5: Experiment 写作思路

## Results 结构 (模式A: 独立Discussion)
- 4.1 Datasets: SRWOV synthetic(30 clips) + real-world(216 clips)
- 4.2 Implementation: 200K iter, 4×A100, T=7, 256×256 crop
- 4.3 Results Analysis:
  - 4.3.1 Quantitative Synthetic
  - 4.3.2 Quantitative Real-world
  - 4.3.3 Qualitative Comparison
- 4.4 Ablation Study (w/o命名, 交叉引用Discussion)
- 4.5 Hyperparameter Sensitivity
- 4.6 Complexity Analysis

## 关键数据
- MgfrOFR vs MambaOFR: +2.13dB PSNR (Wilcoxon p=3.7e-09)
- 复杂度: +0.011M params (+0.32%), +14.1G FLOPs (+0.50%)
- 诚实性决策: LPIPS/DISTS方向一致但未达显著，如实报告

## Discussion 关键发现
- Train-test inversion: B训练最优→测试最差
- RATR强制分支解耦: 牺牲训练loss换泛化
- Branch specialization: SSM-Conv 0.12, SSM-Attn 0.11, Conv-Attn 0.37 (验证多样性)
