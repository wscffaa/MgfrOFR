# reidmamba Baseline 决策报告

> **Phase**: 1
> **生成时间**: 2026-03-22
> **决策方式**: 论文与代码证据复核

## 决策结果

**推荐 Baseline**: **MambaOFR**

## 决策依据

1. 论文把 ReIDMamba 明确定义为“pure Mamba-based”框架，且所有核心改动都建立在多 class token + BiMamba 主干之上，见 `projects/001-reidmamba/ref_latex/GranRankMamba.md:5-8,62-62,107-185`。
2. `MGFE` 的工程实现直接复用共享 Mamba 主干并在后两层分叉，见 `projects/001-reidmamba/ref_code/reidmamba.py:181-238,259-316`。这和 `MambaOFR` 现有 `forward_resblocks` / `backward_resblocks` 的双向 Mamba body 最接近，见 `framework/basicofr/archs/mambaofr_arch.py:89-115,186-218`。
3. `RATR` 只依赖多分支输出特征，不依赖 CNN/Transformer 特有结构；`MambaOFR` 保留 Mamba 主干，最容易挂接这类训练期正则。
4. `RTN` 与 `RRTN` 都会先把问题退化成“先换 backbone 再迁移创新”，这不是最小改动路径。

## 证据表

| 证据项 | 结论 | 来源 |
|------|------|------|
| 主体架构是否为纯 Mamba | 是 | `projects/001-reidmamba/ref_latex/GranRankMamba.md:5-8` |
| 核心创新是否依赖多分支 Mamba 表征 | 是 | `projects/001-reidmamba/ref_latex/GranRankMamba.md:107-185` |
| 代码是否共享主干后再分叉 | 是 | `projects/001-reidmamba/ref_code/reidmamba.py:181-238` |
| OFR 中是否已有双向 Mamba body 可承接 | 是 | `framework/basicofr/archs/mambaofr_arch.py:92-115,186-218` |

## 共识状态

- **状态**: `已收敛`
- **结论**: `MambaOFR` 是唯一合理的首选基线
- **排除结论**: `RTN`/`RRTN` 仅可作为远端参考，不适合作为本轮集成 baseline

## 下一步

- 以 `MambaOFR` 为基础筛选真正可迁移创新，只保留 `MGFE` 与 `RATR`
- 在 `03-SCI-故事线.md` 和 `04-框架对齐.md` 中统一方法名为 `MGFROFR`
