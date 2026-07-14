## 消融矩阵（reidmamba）

> **Baseline**: `MambaOFR`
> **方法名**: `MGFROFR`
> **创新模块数**: 2
> **变体数**: 4

### 创新模块清单

| ID | 名称 | 类型 | 说明 |
|----|------|------|------|
| A | `MGFE` | `attention/ssm` | 在 `MambaOFR` body 后构造多粒度 restoration token 分支 |
| B | `RATR` | `loss/regularization` | 对多分支特征施加排序感知多样性正则 |

### 消融变体矩阵

| ID | 变体名称 | 模块组合 | 目标 |
|----|----------|----------|------|
| `A0` | `baseline_mambaofr` | 无创新模块 | 提供 `MambaOFR` 纯基线参照 |
| `A1` | `plus_mgfe` | `MGFE` | 验证多粒度特征提取本身是否有效 |
| `A2` | `plus_ratr` | `RATR` | 验证排序感知正则是否能独立提升训练稳定性与特征互补性 |
| `A3` | `full_mgfrofr` | `MGFE + RATR` | 验证结构与正则的组合收益 |

### 配置文件映射

```yaml
# framework/options/train/mgfrofr/
# A0: mgfrofr_a0.yml -> network_g.type: MambaOFRNet
# A1: mgfrofr_a1.yml -> network_g.type: MgfrOFR, use_mgfe: true, use_ratr: false
# A2: mgfrofr_a2.yml -> network_g.type: MgfrOFR, use_mgfe: false, use_ratr: true
# A3: mgfrofr_a3.yml -> network_g.type: MgfrOFR, use_mgfe: true, use_ratr: true
```
