# Step 4: 改 Introduction + Method

## Introduction 修改
- 语气收敛为 Applied Sciences 风格: "背景→挑战→方法概述→图→贡献"
- 贡献列表精简，每项1-2句
- 删单独 Notation 表（打断MDPI收尾感）

## Method 修改
- 新增 "3.2 Core Restoration Modules" 层级，含 3.2.1 MGFE / 3.2.2 RATR
- 16+公式密集但每个都有功能，精简而非删除
- max vs mean fusion 引用ReIDMamba实验结果为依据

## 实验状态
- 4个消融变体全部训练完毕 (200K each)
- 训练末期关键发现: B(MGFE only)训练L_perc最低(0.608)但测试LPIPS最差(+75%)
- Train-test inversion: branch collapse找到VGG/判别器shortcut
