# reidmamba - code scan（Phase 0）

> 产出者：人工复核
> 扫描范围：论文主文稿 + 参考实现 + OFR 基线

## 核心文件与入口

- `projects/001-reidmamba/ref_latex/GranRankMamba.md`: 论文主文稿，给出 `MGFE`、`RATR` 的定义与公式
- `projects/001-reidmamba/ref_code/reidmamba.py`: `ReIDMamba` 主体实现，多分支与 class token 融合逻辑在此
- `framework/basicofr/archs/mambaofr_arch.py`: `MambaOFR` 基线，后续挂载目标

## 关键模块定位

| 模块 | file:line | 论文章节 | 备注 |
|------|-----------|----------|------|
| 多 class token 基线 | `projects/001-reidmamba/ref_code/reidmamba.py:129-166,240-247` | `§III-A` | 均匀插入 class token，属于 baseline 设计 |
| `MGFE` 初始化 | `projects/001-reidmamba/ref_code/reidmamba.py:199-238` | `§III-B` | `G` 分支、降采样 token 索引、每支独立 neck |
| `MGFE` 前向 | `projects/001-reidmamba/ref_code/reidmamba.py:259-316` | `§III-B` | 按 `2^g` 融合 class token，再走 2 层 BiMB |
| 多分支输出接口 | `projects/001-reidmamba/ref_code/reidmamba.py:318-335` | `§III-C` | 训练时返回分支特征；`RATR` 可消费这里的输出 |
| `RATR` 公式 | `projects/001-reidmamba/ref_latex/GranRankMamba.md:141-185` | `§III-C` | 公开 `ref_code` 未出现显式 `RATR` loss 实现 |
| `MambaOFR` body | `framework/basicofr/archs/mambaofr_arch.py:92-115,186-218` | - | `MGFE` 的直接挂载位置 |

## 贡献点标记

- `MGFE` 是实打实的结构创新，代码与论文都能对上。
- `RATR` 是实打实的训练创新，但当前参考代码仓没有给出显式损失实现，只能按论文重写。
- `OverlapPatchEmbed`、`GeneralizedMean`、`TokenFusion` 只应当作为工具或内部细节记录，不应再被写成主创新。

## 依赖与风险

- `4D/5D` 边界：`MambaOFR` 是视频特征图，`ReIDMamba` 是 token 序列，必须显式做 adapter。
- 显存风险：`MGFE` 的分支数和 token 数会线性增加中间激活。
- 数值风险：`RATR` 的 `D-KTau` 需要稳定实现，先做小 batch 冒烟。
- 第三方依赖：`PyTorch`、`mamba-ssm`、`einops`；无需为 `RATR` 新增特殊依赖。

## 建议集成 baseline 与挂载点

- baseline：`MambaOFR`
- 结构挂载：`framework/basicofr/archs/mambaofr_arch.py:186,218`
- loss 挂载：参考 `framework/basicofr/models/wavemamba_model.py:27-33,129-138`
