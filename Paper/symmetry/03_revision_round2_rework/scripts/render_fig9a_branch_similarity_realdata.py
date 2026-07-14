#!/usr/bin/env python3
"""Render Fig. 9a from archived 30-clip branch-similarity measurements."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


SCRIPT_PATH = Path(__file__).resolve()
ROUND2_DIR = SCRIPT_PATH.parents[1]
PROJECT_DIR = SCRIPT_PATH.parents[4]
EVIDENCE_DIR = ROUND2_DIR / "evidence"
FIGURE_DIR = ROUND2_DIR / "source" / "figures"

A1_JSON = (
    PROJECT_DIR
    / "Paper"
    / "writing"
    / "review"
    / "round1"
    / "t5-figures"
    / "evidence"
    / "branch_sim_evolution_a1_20260630.json"
)
F1_JSON = (
    PROJECT_DIR
    / "Paper"
    / "writing"
    / "review"
    / "round1"
    / "t5-figures"
    / "evidence"
    / "branch_sim_evolution_f1_20260630.json"
)

OUTPUT_PDF = FIGURE_DIR / "Fig9a_branch_similarity.pdf"
OUTPUT_SVG = EVIDENCE_DIR / "Fig9a_branch_similarity_realdata.svg"
OUTPUT_PNG = EVIDENCE_DIR / "Fig9a_branch_similarity_realdata_preview.png"
OUTPUT_GRAY = EVIDENCE_DIR / "Fig9a_branch_similarity_realdata_grayscale.png"
SUMMARY_JSON = EVIDENCE_DIR / "fig9a_branch_similarity_realdata_summary.json"
PLOT_DATA_CSV = EVIDENCE_DIR / "fig9a_branch_similarity_realdata_plotdata.csv"

BRANCH_LABELS = ["Fine", "Medium", "Coarse"]
COLOR_MGFE = "#E69F00"
COLOR_FULL = "#0072B2"
GRID_COLOR = "#D8DDE3"


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if data.get("num_clips") != 30:
        raise ValueError(f"{path} does not contain the expected 30-clip protocol")
    points = data.get("points", [])
    if not points:
        raise ValueError(f"{path} has no checkpoint points")
    return data


def _point_by_iter(data: dict, iteration: int) -> dict:
    for point in data["points"]:
        if int(point["iter"]) == iteration:
            return point
    raise ValueError(f"missing {iteration} checkpoint for {data.get('variant')}")


def _offdiag_values(matrix: np.ndarray) -> list[float]:
    return [
        float(matrix[0, 1]),
        float(matrix[0, 2]),
        float(matrix[1, 2]),
    ]


def _draw_heatmap(ax, matrix: np.ndarray, title: str, subtitle: str, panel: str):
    image = ax.imshow(matrix, vmin=0.0, vmax=1.0, cmap="cividis")
    ax.set_xticks(range(3), BRANCH_LABELS, rotation=35, ha="right")
    ax.set_yticks(range(3), BRANCH_LABELS)
    ax.tick_params(axis="both", length=0, labelsize=7.5)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title(f"{title}\n{subtitle}", fontsize=8.5, pad=4)
    ax.text(
        -0.28,
        1.17,
        panel,
        transform=ax.transAxes,
        fontsize=10,
        fontweight="bold",
        ha="left",
        va="top",
    )

    for i in range(3):
        for j in range(3):
            value = matrix[i, j]
            color = "black" if value > 0.45 else "white"
            ax.text(j, i, f"{value:.2f}", ha="center", va="center", fontsize=7.5, color=color)

    ax.set_xticks(np.arange(-0.5, 3, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 3, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=0.8)
    ax.tick_params(which="minor", bottom=False, left=False)
    return image


def _extract_series(data: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    points = sorted(data["points"], key=lambda p: int(p["iter"]))
    x = np.array([int(p["iter"]) // 1000 for p in points], dtype=float)
    mean = np.array([float(p["off_diag_mean"]) for p in points], dtype=float)
    std = np.array([float(p["off_diag_std"]) for p in points], dtype=float)
    return x, mean, std


def _write_plot_data(a1: dict, f1: dict) -> None:
    rows = []
    for label, data in [("MGFE-only", a1), ("MgfrOFR full", f1)]:
        for point in sorted(data["points"], key=lambda p: int(p["iter"])):
            rows.append(
                {
                    "variant": label,
                    "iteration": int(point["iter"]),
                    "checkpoint_k": int(point["iter"]) // 1000,
                    "mean_offdiag_cosine": float(point["off_diag_mean"]),
                    "sd_offdiag_cosine": float(point["off_diag_std"]),
                    "clips": int(point["clips"]),
                }
            )
    with PLOT_DATA_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _save_grayscale_preview() -> None:
    image = plt.imread(OUTPUT_PNG)
    rgb = image[..., :3]
    if image.shape[-1] == 4:
        alpha = image[..., 3:4]
        rgb = rgb * alpha + (1.0 - alpha)
    gray = 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]
    plt.imsave(OUTPUT_GRAY, gray, cmap="gray", vmin=0.0, vmax=1.0)


def main() -> None:
    a1 = _load(A1_JSON)
    f1 = _load(F1_JSON)
    a1_final = _point_by_iter(a1, 200000)
    f1_final = _point_by_iter(f1, 200000)
    a1_matrix = np.array(a1_final["sim_matrix"], dtype=float)
    f1_matrix = np.array(f1_final["sim_matrix"], dtype=float)

    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "font.size": 8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
            "axes.linewidth": 0.6,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "legend.frameon": False,
        }
    )

    fig = plt.figure(figsize=(7.0, 2.50), constrained_layout=False)
    grid = fig.add_gridspec(
        1,
        4,
        width_ratios=[1.02, 1.02, 0.040, 1.72],
        left=0.065,
        right=0.965,
        top=0.84,
        bottom=0.25,
        wspace=0.52,
    )

    ax_a1 = fig.add_subplot(grid[0, 0])
    ax_f1 = fig.add_subplot(grid[0, 1])
    cax = fig.add_subplot(grid[0, 2])
    ax_line = fig.add_subplot(grid[0, 3])

    image = _draw_heatmap(
        ax_a1,
        a1_matrix,
        "MGFE-only",
        f"200K, mean {a1_final['off_diag_mean']:.3f}",
        "a",
    )
    _draw_heatmap(
        ax_f1,
        f1_matrix,
        "MgfrOFR full",
        f"200K, mean {f1_final['off_diag_mean']:.3f}",
        "b",
    )
    cbar = fig.colorbar(image, cax=cax)
    cbar.set_ticks([0.0, 0.5, 1.0])
    cbar.set_ticklabels(["0", "0.5", "1.0"])
    cbar.ax.tick_params(labelsize=7, width=0.5, length=2)
    cbar.set_label("Cosine", fontsize=7.2, labelpad=6)
    cbar.ax.yaxis.set_label_position("left")

    a1_x, a1_mean, a1_std = _extract_series(a1)
    f1_x, f1_mean, f1_std = _extract_series(f1)
    ax_line.errorbar(
        a1_x,
        a1_mean,
        yerr=a1_std,
        marker="o",
        markersize=3.5,
        linewidth=1.25,
        linestyle="-",
        capsize=2.2,
        color=COLOR_MGFE,
    )
    ax_line.errorbar(
        f1_x,
        f1_mean,
        yerr=f1_std,
        marker="s",
        markersize=3.5,
        linewidth=1.25,
        linestyle="--",
        capsize=2.2,
        color=COLOR_FULL,
    )
    ax_line.text(
        -0.14,
        1.17,
        "c",
        transform=ax_line.transAxes,
        fontsize=10,
        fontweight="bold",
        ha="left",
        va="top",
    )
    ax_line.set_title("Mean off-diagonal cosine (30 clips)", fontsize=8.5, pad=4)
    ax_line.set_xlabel("Checkpoint (K iterations)", fontsize=7.5)
    ax_line.set_xticks(a1_x)
    ax_line.set_xlim(45, 248)
    ax_line.set_ylim(0.0, 1.0)
    ax_line.set_yticks([0.0, 0.25, 0.50, 0.75, 1.0])
    ax_line.grid(True, axis="y", linewidth=0.45, color=GRID_COLOR)
    ax_line.tick_params(axis="both", labelsize=7.5, width=0.5, length=2.5)
    ax_line.annotate(
        "MGFE-only",
        xy=(a1_x[-1], a1_mean[-1]),
        xytext=(7, 0),
        textcoords="offset points",
        fontsize=7.2,
        color=COLOR_MGFE,
        ha="left",
        va="center",
    )
    ax_line.annotate(
        "MgfrOFR full",
        xy=(f1_x[-1], f1_mean[-1]),
        xytext=(7, 0),
        textcoords="offset points",
        fontsize=7.2,
        color=COLOR_FULL,
        ha="left",
        va="center",
    )
    for spine in ["top", "right"]:
        ax_line.spines[spine].set_visible(False)

    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    _write_plot_data(a1, f1)
    fig.savefig(OUTPUT_PDF)
    fig.savefig(OUTPUT_SVG)
    fig.savefig(OUTPUT_PNG, dpi=300)
    plt.close(fig)
    _save_grayscale_preview()

    a1_offdiag = _offdiag_values(a1_matrix)
    f1_offdiag = _offdiag_values(f1_matrix)
    summary = {
        "figure": "Fig9a_branch_similarity",
        "data_source": {
            "a1_json": str(A1_JSON),
            "a1_sha256": _sha256(A1_JSON),
            "f1_json": str(F1_JSON),
            "f1_sha256": _sha256(F1_JSON),
        },
        "protocol": {
            "dataset": a1["dataset"],
            "num_clips": a1["num_clips"],
            "metric": a1["metric"],
            "checkpoints": [int(p["iter"]) for p in sorted(a1["points"], key=lambda p: int(p["iter"]))],
        },
        "final_200k": {
            "mgfe_only": {
                "mean": float(a1_final["off_diag_mean"]),
                "std": float(a1_final["off_diag_std"]),
                "offdiag_min": min(a1_offdiag),
                "offdiag_max": max(a1_offdiag),
                "matrix": a1_final["sim_matrix"],
            },
            "mgfrofr_full": {
                "mean": float(f1_final["off_diag_mean"]),
                "std": float(f1_final["off_diag_std"]),
                "offdiag_min": min(f1_offdiag),
                "offdiag_max": max(f1_offdiag),
                "matrix": f1_final["sim_matrix"],
            },
        },
        "outputs": {
            "pdf": str(OUTPUT_PDF),
            "svg": str(OUTPUT_SVG),
            "png_preview": str(OUTPUT_PNG),
            "grayscale_preview": str(OUTPUT_GRAY),
            "plot_data_csv": str(PLOT_DATA_CSV),
        },
    }
    SUMMARY_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary["final_200k"], indent=2))
    print(f"wrote {OUTPUT_PDF}")
    print(f"wrote {SUMMARY_JSON}")


if __name__ == "__main__":
    main()
