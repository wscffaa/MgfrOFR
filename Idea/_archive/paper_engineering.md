# reidmamba - paper engineering（Phase 0）

> 产出者：人工复核
> 自动提取：已人工补全

## 论文信息

- **标题**: ReIDMamba: Learning Discriminative Features with Visual State Space Model for Person Re-Identification
- **摘要概括**: 论文以纯 Mamba 为主干，先用多 class token 构造强基线，再通过 `MGFE` 提取多粒度特征，通过 `RATR` 压低多分支排序相关性，最终在 Person ReID 上提升判别性与效率。

## 章节结构

- `§III-A`: Mamba-based strong baseline with multiple class tokens
- `§III-B`: `MGFE`
- `§III-C`: `RATR`
- `§III-D`: Training and inference
- `§IV-D`: Ablation of `MGFE` / `RATR`

## 贡献点与 novelty

1. 多 class token 强基线为纯 Mamba ReID 提供细粒度全局表示，但这是 baseline 设计，不是本轮要抽取的核心创新。
2. `MGFE` 才是核心结构创新，它把单粒度特征扩展成多分支、多粒度表示。
3. `RATR` 才是核心训练创新，它从排序相关性而非简单正交性出发，约束多分支特征多样性。

## 与 OFR Baseline 的差异

- `RTN`：主干不是 Mamba，迁移 `MGFE/RATR` 会额外叠加 backbone 变更，不适合作为首选基线。
- `RRTN`：过于偏向原有 Transformer/关系建模设计，与论文“纯 Mamba”前提不对齐。
- `MambaOFR`：已有双向 `MambaIR` body，可直接承接 `MGFE` 的多分支逻辑与 `RATR` 的训练期正则。

## 可迁移创新点候选

- `MGFE`：收益假设是增强多尺度损伤与结构纹理的分解建模；风险是 `4D/5D <-> token` 适配；最小验证是 `A1` 对比 `A0`。
- `RATR`：收益假设是减少多分支冗余；风险是 OFR 正负样本定义需要重写；最小验证是 `A2` 与 `A3` 对比分支相关性与重建指标。
- `OverlapPatchEmbed` / `GeneralizedMean` / `TokenFusion`：只作为实现细节记录，不再作为独立可迁移创新。
