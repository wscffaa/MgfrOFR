# MgfrOFR

[![Status](https://img.shields.io/badge/status-pre--acceptance--preview-lightgrey.svg)](#release-policy)
[![License](https://img.shields.io/badge/License-Apache--2.0-green.svg)](LICENSE)

Official repository for **Multi-Granularity Feature Decomposition with Ranking-Aware Regularization for Old Film Restoration**.

> This is a pre-acceptance public preview repository. The implementation, pretrained models, training configs, and evaluation scripts will be released after the paper is accepted or when the review policy permits code release.

## Overview

MgfrOFR targets old-film restoration, where frames may contain mixed analog degradations such as scratches, dust, noise, blur, flicker, local defects, and temporal inconsistency.

The method is designed around two ideas:

- **Multi-granularity feature decomposition** for separating restoration cues at different degradation scales.
- **Ranking-aware regularization** for encouraging temporally stable restoration behavior during training.

## Release Policy

To avoid exposing implementation details during peer review, this repository currently contains only public-facing metadata and release notes.

The following assets are intentionally withheld before acceptance:

- source code;
- model architecture implementation;
- training and testing scripts;
- detailed YAML configs;
- pretrained checkpoints;
- raw experiment logs;
- ablation internals.

After acceptance, this repository will be updated with a full reproducible release.

## Planned Release Contents

```text
MgfrOFR/
├── mgfrofr/              # model architecture and loss implementation
├── options/              # train/test configs
├── scripts/              # training, testing, and inference entry points
├── docs/                 # dataset, model-zoo, and result documentation
├── tests/                # smoke tests
├── README.md
├── LICENSE
└── CITATION.cff
```

## Roadmap

- [ ] Add paper link.
- [ ] Release source code after acceptance.
- [ ] Release pretrained models and SHA256 checksums.
- [ ] Add dataset preparation instructions.
- [ ] Add training, evaluation, and inference commands.
- [ ] Add final benchmark tables after metric provenance is frozen.
- [ ] Add qualitative examples and teaser figure.

## Dataset

The method is evaluated in the old-film restoration setting with synthetic REDS-style degraded videos and real-world old-film clips. Detailed dataset preparation instructions will be released together with the code.

This repository does not redistribute third-party datasets.

## Model Zoo

Pretrained weights are not included in this pre-acceptance preview. After release, model files will be distributed through GitHub Releases, Zenodo, Hugging Face, or another persistent storage provider with checksums.

## Citation

Please cite the paper if this project is useful for your research. The final BibTeX entry will be updated after publication.

```bibtex
@article{cai2026mgfrofr,
  title={Multi-Granularity Feature Decomposition with Ranking-Aware Regularization for Old Film Restoration},
  author={Cai, Feifan},
  year={2026}
}
```

A machine-readable citation file is provided in [CITATION.cff](CITATION.cff).

## Contact

For questions before the full code release, please open an issue in this repository.

## License

This metadata preview is released under the [Apache License 2.0](LICENSE). The full code release will use the same repository unless paper/review constraints require adjustment.
