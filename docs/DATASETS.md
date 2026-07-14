# Dataset Preparation

This repository expects REDS-derived synthetic old-film data and SRWOV real-world evaluation clips under `datasets/OldFilmRestoration/`.

The repository does not redistribute REDS, SRWOV, or third-party datasets. Download datasets from their official sources and arrange them according to the layout in `README.md`.

Training uses REDS frames plus degradation templates under `datasets/OldFilmRestoration/noise_data`. Synthetic evaluation uses paired GT/LQ frames. Real-world evaluation uses LQ-only SRWOV clips.
