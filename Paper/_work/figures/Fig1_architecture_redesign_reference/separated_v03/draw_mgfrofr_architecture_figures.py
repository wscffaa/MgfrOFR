from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle, Circle


OUTDIR = Path(__file__).resolve().parent

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
    "axes.unicode_minus": False,
})

INK = "#243044"
MUTED = "#6B7280"
GRID = "#D7DEE8"
BLUE = "#DDEBFA"
BLUE_E = "#4575B4"
YELLOW = "#FFF4D6"
YELLOW_E = "#D99A00"
GREEN = "#E5F4EA"
GREEN_E = "#4E9F63"
RED = "#FDE8E7"
RED_E = "#D9534F"
PURPLE = "#EEE7F8"
PURPLE_E = "#8064A2"


def setup_canvas(width=7.16, height=2.8, units=(100, 40)):
    fig, ax = plt.subplots(figsize=(width, height))
    fig.patch.set_facecolor("white")
    ax.set_xlim(0, units[0])
    ax.set_ylim(0, units[1])
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, label, fc, ec, fs=8, weight="normal", lw=1.2, ls="-"):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.18,rounding_size=1.0",
        linewidth=lw,
        edgecolor=ec,
        facecolor=fc,
        linestyle=ls,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        label,
        ha="center",
        va="center",
        fontsize=fs,
        color=INK,
        fontweight=weight,
        linespacing=1.12,
    )
    return patch


def label(ax, x, y, text, fs=7, color=INK, ha="center", va="center", weight="normal"):
    ax.text(x, y, text, fontsize=fs, color=color, ha=ha, va=va, fontweight=weight)


def arrow(ax, p0, p1, color=INK, lw=1.2, ls="-", rad=0.0, mutation=9):
    arr = FancyArrowPatch(
        p0,
        p1,
        arrowstyle="-|>",
        mutation_scale=mutation,
        linewidth=lw,
        color=color,
        linestyle=ls,
        connectionstyle=f"arc3,rad={rad}",
        shrinkA=2,
        shrinkB=2,
    )
    ax.add_patch(arr)
    return arr


def tiny_tensor(ax, x, y, w=5.2, h=4.0, color=BLUE_E, fill=BLUE, layers=3):
    for i in range(layers):
        ax.add_patch(Rectangle((x + i * 0.55, y + i * 0.42), w, h, facecolor=fill, edgecolor=color, lw=0.85))
    gx, gy = x + layers * 0.55, y + layers * 0.42
    for k in range(1, 4):
        ax.plot([gx, gx + w], [gy + h * k / 4, gy + h * k / 4], color=color, lw=0.35, alpha=0.55)
        ax.plot([gx + w * k / 4, gx + w * k / 4], [gy, gy + h], color=color, lw=0.35, alpha=0.55)


def frame_tiles(ax, x, y):
    for i, t in enumerate([r"$x_{t-1}$", r"$x_t$", r"$x_{t+1}$"]):
        yy = y + (2 - i) * 4.1
        ax.add_patch(Rectangle((x, yy), 5.6, 3.1, facecolor="#F8FAFC", edgecolor=INK, lw=0.8))
        ax.add_patch(Rectangle((x + 0.35, yy + 0.35), 4.9, 2.4, facecolor="#E5E7EB", edgecolor="#9CA3AF", lw=0.5))
        ax.plot([x + 0.8, x + 2.2, x + 4.6], [yy + 0.7, yy + 2.4, yy + 0.85], color="#94A3B8", lw=0.8)
        label(ax, x + 7.0, yy + 1.55, t, fs=8, ha="left")


def token_row(ax, x, y, n, color, size=1.25, gap=0.42):
    for i in range(n):
        ax.add_patch(Rectangle((x + i * (size + gap), y), size, size, facecolor=color, edgecolor=INK, lw=0.45))


def operator(ax, x, y, text):
    ax.add_patch(Circle((x, y), 1.0, facecolor="white", edgecolor=INK, lw=1.0))
    label(ax, x, y - 0.02, text, fs=7, weight="bold")


def save_all(fig, stem):
    for ext in ("svg", "pdf", "png"):
        path = OUTDIR / f"{stem}.{ext}"
        fig.savefig(path, dpi=320, bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)


def draw_overview():
    fig, ax = setup_canvas(height=2.65, units=(100, 34))
    label(ax, 2, 31.5, "(a) MgfrOFR overview", fs=9, ha="left", weight="bold")

    box(ax, 1.5, 7.0, 10.8, 18.0, "Input\nclip", "#FFFFFF", "#9CA3AF", fs=8)
    frame_tiles(ax, 3.0, 9.0)

    box(ax, 16.0, 12.5, 12.5, 8.8, "MambaOFR\nbackbone", BLUE, BLUE_E, fs=8, weight="bold")
    label(ax, 22.2, 10.6, "unchanged", fs=6.6, color=BLUE_E)

    box(ax, 32.0, 12.5, 13.0, 8.8, "Bidirectional\npropagation", "#F1F7FF", BLUE_E, fs=8)
    label(ax, 38.5, 10.6, r"$f_t^b,\ f_t^f$", fs=7, color=BLUE_E)

    box(ax, 49.0, 10.5, 14.5, 12.8, "MGFE\ncoarse | mid | fine", YELLOW, YELLOW_E, fs=8, weight="bold")
    token_row(ax, 51.0, 13.0, 4, "#FCD34D", size=1.0)
    token_row(ax, 51.0, 16.0, 4, "#C4B5FD", size=1.0)
    token_row(ax, 51.0, 19.0, 4, "#A7F3D0", size=1.0)

    box(ax, 67.0, 12.5, 12.5, 8.8, "Channel-wise\nrecalibration", GREEN, GREEN_E, fs=8)
    box(ax, 83.0, 12.5, 11.8, 8.8, "Reconstruction\nhead", BLUE, BLUE_E, fs=8)
    box(ax, 96.0, 11.2, 3.4, 11.4, r"$y_t$", "#FFFFFF", "#9CA3AF", fs=10, weight="bold")

    for p0, p1 in [
        ((12.4, 16.0), (15.8, 16.0)),
        ((28.6, 16.9), (31.8, 16.9)),
        ((45.1, 16.9), (48.8, 16.9)),
        ((63.7, 16.9), (66.8, 16.9)),
        ((79.7, 16.9), (82.8, 16.9)),
        ((94.9, 16.9), (95.8, 16.9)),
    ]:
        arrow(ax, p0, p1, lw=1.35)

    box(ax, 48.0, 2.2, 32.0, 4.9, "RATR loss: temporal ranking + DiffKendall", RED, RED_E, fs=7.5, ls="--")
    arrow(ax, (56.2, 10.4), (56.2, 7.2), color=RED_E, lw=1.2, ls="--")
    label(ax, 60.5, 8.7, "training only", fs=6.5, color=RED_E)
    label(ax, 88.6, 8.7, "RATR disabled at inference", fs=6.5, color=RED_E)

    save_all(fig, "fig1_overview_cvpr_vector")


def draw_mgfe():
    fig, ax = setup_canvas(height=3.05, units=(100, 42))
    label(ax, 2, 39.5, "(b) MGFE: multi-granularity feature extraction", fs=9, ha="left", weight="bold")

    box(ax, 2.0, 17.8, 11.5, 7.0, r"$f_t$" + "\nfeature map", BLUE, BLUE_E, fs=8, weight="bold")
    tiny_tensor(ax, 5.0, 19.0, w=3.3, h=2.6)
    box(ax, 17.0, 17.8, 12.0, 7.0, "Flatten\nimage tokens", "#F8FAFC", "#94A3B8", fs=8)
    token_row(ax, 19.0, 19.8, 6, "#DBEAFE", size=1.0)

    box(ax, 33.0, 15.5, 20.0, 11.5, "Token insertion\nM=12 restoration tokens", YELLOW, YELLOW_E, fs=8, weight="bold")
    token_row(ax, 36.0, 18.2, 9, "#DBEAFE", size=0.72, gap=0.25)
    for i in [2, 5, 8]:
        ax.add_patch(Rectangle((36.0 + i * 0.97, 21.3), 0.72, 0.72, facecolor="#FCD34D", edgecolor=INK, lw=0.4))
    label(ax, 43.0, 23.8, "uniform positions", fs=6.4, color=MUTED)

    group = FancyBboxPatch((56.0, 7.0), 24.5, 28.0, boxstyle="round,pad=0.2,rounding_size=1.1",
                           facecolor="#FFFFFF", edgecolor=YELLOW_E, lw=1.0, linestyle="--")
    ax.add_patch(group)
    label(ax, 68.2, 33.0, "progressive fusion", fs=8, weight="bold", color=YELLOW_E)
    lanes = [("Coarse", "#FDE68A", 4, 26), ("Medium", "#DDD6FE", 6, 20), ("Fine", "#A7F3D0", 9, 14)]
    for name, col, n, yy in lanes:
        token_row(ax, 58.5, yy, n, col, size=0.9, gap=0.25)
        arrow(ax, (70.0, yy + 0.45), (74.5, yy + 0.45), lw=1.0)
        box(ax, 75.0, yy - 1.0, 4.2, 2.9, name, col, "#64748B", fs=6.8)

    box(ax, 84.0, 22.8, 10.0, 5.5, r"$B_t$" + "\nbranch descriptors", PURPLE, PURPLE_E, fs=7.5)
    box(ax, 84.0, 13.2, 10.0, 5.5, r"$\gamma_t,\ \beta_t$" + "\nscale / shift", GREEN, GREEN_E, fs=7.5)
    box(ax, 84.0, 4.0, 10.0, 5.5, r"$\tilde{f}_t$" + "\nrecalibrated", BLUE, BLUE_E, fs=7.5)

    for p0, p1 in [
        ((13.7, 21.3), (16.8, 21.3)),
        ((29.2, 21.3), (32.8, 21.3)),
        ((53.2, 21.3), (55.8, 21.3)),
        ((79.5, 24.5), (83.8, 25.4)),
        ((89.0, 22.7), (89.0, 18.9)),
        ((89.0, 13.0), (89.0, 9.7)),
    ]:
        arrow(ax, p0, p1, lw=1.2)

    label(ax, 95.5, 8.8, "same shape", fs=6.5, color=MUTED, ha="left")
    save_all(fig, "fig2_mgfe_cvpr_vector")


def draw_ratr():
    fig, ax = setup_canvas(height=2.65, units=(100, 34))
    label(ax, 2, 31.5, "(c) RATR: ranking-aware training regularizer", fs=9, ha="left", weight="bold")

    box(ax, 3.0, 12.0, 14.0, 9.0, r"$B_t$" + "\nbranch descriptors", PURPLE, PURPLE_E, fs=8, weight="bold")
    label(ax, 10.0, 10.0, r"$N_b \times T \times G \times D$", fs=6.5, color=MUTED)

    group = FancyBboxPatch((22.0, 7.0), 24.0, 20.0, boxstyle="round,pad=0.2,rounding_size=1.0",
                           facecolor="#FFFFFF", edgecolor=RED_E, lw=1.0, linestyle="--")
    ax.add_patch(group)
    label(ax, 34.0, 24.8, "temporal ranking", fs=8, weight="bold", color=RED_E)
    for i, yy in enumerate([20.5, 17.0, 13.5]):
        label(ax, 24.0, yy, ["t-1", "t", "t+1"][i], fs=6.8, ha="left")
        ax.plot([29, 42], [yy, yy], color=INK, lw=0.85)
        for x, c in zip([31, 35, 39], ["#93C5FD", "#A7F3D0", "#FCA5A5"]):
            ax.add_patch(Circle((x, yy), 0.65, facecolor=c, edgecolor=INK, lw=0.45))
    label(ax, 34.5, 10.0, "positive / negative ranks", fs=6.4, color=MUTED)

    box(ax, 51.0, 10.5, 15.0, 12.0, "DiffKendall\nrank correlation", RED, RED_E, fs=8, weight="bold")
    for r in range(5):
        for c in range(5):
            shade = 0.18 + 0.11 * abs(r - c)
            ax.add_patch(Rectangle((54.2 + c * 1.4, 12.5 + r * 1.4), 1.15, 1.15,
                                   facecolor=(1.0, 0.2 + shade, 0.2 + shade), edgecolor="white", lw=0.2))

    box(ax, 72.0, 12.0, 11.5, 9.0, r"$\mathcal{L}_{intra}$" + "\n" + r"$\mathcal{L}_{inter}$", "#FFFFFF", RED_E, fs=9, weight="bold")
    box(ax, 88.0, 12.0, 9.0, 9.0, "total\nloss", "#FFFFFF", "#9CA3AF", fs=8)

    for p0, p1 in [
        ((17.3, 16.5), (21.8, 16.5)),
        ((46.2, 16.5), (50.8, 16.5)),
        ((66.2, 16.5), (71.8, 16.5)),
        ((83.7, 16.5), (87.8, 16.5)),
    ]:
        arrow(ax, p0, p1, lw=1.25)
    operator(ax, 85.7, 16.5, "+")

    label(ax, 50.0, 4.8, "training only; disabled at inference", fs=7, color=RED_E, weight="bold")
    ax.plot([23, 83], [5.9, 5.9], color=RED_E, lw=1.0, ls="--")

    save_all(fig, "fig3_ratr_cvpr_vector")


def main():
    draw_overview()
    draw_mgfe()
    draw_ratr()


if __name__ == "__main__":
    main()
