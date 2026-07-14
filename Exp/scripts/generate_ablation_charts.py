#!/usr/bin/env python3
"""从 TensorBoard 事件文件提取数据并生成消融对比图表。

生成:
  1. PSNR 对比曲线 (4 变体叠加)
  2. SSIM 对比曲线 (4 变体叠加)
  3. GAN Loss 对比面板 (l_g_pix + l_g_percep + l_g_gan)
  4. 判别器 Loss 对比面板 (l_d_real + l_d_fake)

输出到: projects/001-reidmamba/Exp/charts/
"""

import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# ─── Configuration ───────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TB_BASE = os.path.join(BASE_DIR, "experiments")
CHART_DIR = os.path.join(BASE_DIR, "charts")
METRICS_FILE = os.path.join(BASE_DIR, "metrics_history.json")

VARIANTS = {
    "mgfrofr_a0_baseline": {"label": "A0 Baseline", "color": "#6366f1", "marker": "o"},
    "mgfrofr_a1_mgfe":     {"label": "A1 +MGFE",    "color": "#f59e0b", "marker": "s"},
    "mgfrofr_a2_ratr":     {"label": "A2 +RATR",    "color": "#ef4444", "marker": "^"},
    "mgfrofr_a3_full":     {"label": "A3 Full",     "color": "#10b981", "marker": "D"},
}

# ─── Style ───────────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor': '#0f172a',
    'axes.facecolor': '#1e293b',
    'axes.edgecolor': '#334155',
    'axes.labelcolor': '#e2e8f0',
    'text.color': '#e2e8f0',
    'xtick.color': '#94a3b8',
    'ytick.color': '#94a3b8',
    'grid.color': '#334155',
    'grid.alpha': 0.5,
    'legend.facecolor': '#1e293b',
    'legend.edgecolor': '#475569',
    'legend.fontsize': 10,
    'font.size': 11,
    'font.family': 'sans-serif',
})

def load_tb_scalars(variant_name, tag):
    """Load scalar data from TensorBoard events."""
    from tensorboard.backend.event_processing import event_accumulator
    tb_dir = os.path.join(TB_BASE, variant_name, "tb_logger", variant_name)
    if not os.path.isdir(tb_dir):
        return [], []
    ea = event_accumulator.EventAccumulator(tb_dir, size_guidance={'scalars': 0})
    ea.Reload()
    if tag not in ea.Tags().get('scalars', []):
        return [], []
    events = ea.Scalars(tag)
    steps = [e.step for e in events]
    values = [e.value for e in events]
    return steps, values

def load_metrics_json():
    """Load validation metrics from metrics_history.json."""
    with open(METRICS_FILE) as f:
        data = json.load(f)
    result = {}
    for vname, v in data['variants'].items():
        cps = v.get('checkpoints', [])
        iters = [cp['iter'] for cp in cps]
        psnr = [cp.get('psnr', 0) for cp in cps]
        ssim = [cp.get('ssim', 0) for cp in cps]
        result[vname] = {'iters': iters, 'psnr': psnr, 'ssim': ssim, 'label': v.get('label', vname)}
    return result

def smooth(values, weight=0.9):
    """Exponential moving average smoothing."""
    smoothed = []
    last = values[0] if values else 0
    for v in values:
        smoothed_val = last * weight + (1 - weight) * v
        smoothed.append(smoothed_val)
        last = smoothed_val
    return smoothed

def format_iter(x, _):
    """Format iteration number as 'Nk'."""
    if x >= 1000:
        return f'{x/1000:.0f}k'
    return f'{x:.0f}'

def plot_metric_comparison(metric_name, ylabel, filename, ylim=None):
    """Plot validation metric comparison for all 4 variants."""
    fig, ax = plt.subplots(figsize=(14, 6))
    
    metrics = load_metrics_json()
    
    for vname, cfg in VARIANTS.items():
        if vname in metrics:
            m = metrics[vname]
            iters = np.array(m['iters']) / 1000  # Convert to k
            vals = m[metric_name]
            
            # Plot line with markers
            ax.plot(iters, vals, color=cfg['color'], marker=cfg['marker'],
                    markersize=5, linewidth=1.5, alpha=0.8, label=cfg['label'])
            
            # Highlight best point
            best_idx = np.argmax(vals)
            ax.scatter([iters[best_idx]], [vals[best_idx]], 
                      color=cfg['color'], s=120, zorder=5, edgecolors='white',
                      linewidths=2)
            ax.annotate(f'{vals[best_idx]:.2f}',
                       (iters[best_idx], vals[best_idx]),
                       textcoords="offset points", xytext=(0, 12),
                       ha='center', fontsize=9, fontweight='bold',
                       color=cfg['color'],
                       bbox=dict(boxstyle='round,pad=0.2', facecolor='#0f172a',
                                edgecolor=cfg['color'], alpha=0.8))
    
    ax.set_xlabel('Iteration (k)', fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(f'{ylabel} Comparison — MGFROFR Ablation Study', fontsize=14, fontweight='bold')
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.0f}k'))
    ax.legend(loc='lower right', framealpha=0.9)
    ax.grid(True, linestyle='--', alpha=0.3)
    
    if ylim:
        ax.set_ylim(ylim)
    
    plt.tight_layout()
    filepath = os.path.join(CHART_DIR, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  ✅ {filepath}")
    return filepath

def plot_loss_curves():
    """Plot GAN loss curves from TensorBoard events."""
    loss_groups = {
        'generator_losses': {
            'title': 'Generator Losses',
            'tags': ['losses/l_g_pix', 'losses/l_g_percep', 'losses/l_g_gan'],
            'labels': ['L_pixel', 'L_perceptual', 'L_GAN'],
        },
        'discriminator_losses': {
            'title': 'Discriminator Losses',
            'tags': ['losses/l_d_real', 'losses/l_d_fake', 'losses/l_d'],
            'labels': ['L_D_real', 'L_D_fake', 'L_D_total'],
        }
    }
    
    for group_name, group_cfg in loss_groups.items():
        fig, axes = plt.subplots(2, 2, figsize=(16, 10))
        fig.suptitle(f'{group_cfg["title"]} — All Variants', fontsize=16, fontweight='bold', y=0.98)
        
        for ax_idx, (vname, vcfg) in enumerate(VARIANTS.items()):
            ax = axes[ax_idx // 2][ax_idx % 2]
            
            for tag, tag_label in zip(group_cfg['tags'], group_cfg['labels']):
                steps, values = load_tb_scalars(vname, tag)
                if steps:
                    # Subsample for performance (every 100th point)
                    n = max(1, len(steps) // 500)
                    steps_sub = steps[::n]
                    values_smooth = smooth(values[::n], weight=0.95)
                    
                    iters_k = [s / 1000 for s in steps_sub]
                    ax.plot(iters_k, values_smooth, linewidth=1.2, alpha=0.85, label=tag_label)
            
            ax.set_title(vcfg['label'], fontsize=12, fontweight='bold', color=vcfg['color'])
            ax.set_xlabel('Iteration (k)')
            ax.set_ylabel('Loss')
            ax.legend(fontsize=8, loc='upper right')
            ax.grid(True, linestyle='--', alpha=0.3)
        
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        filepath = os.path.join(CHART_DIR, f'{group_name}.png')
        fig.savefig(filepath, dpi=150, bbox_inches='tight')
        plt.close(fig)
        print(f"  ✅ {filepath}")

def plot_ratr_loss():
    """Plot RATR loss for A2 and A3 variants."""
    fig, ax = plt.subplots(figsize=(14, 5))
    
    for vname in ['mgfrofr_a2_ratr', 'mgfrofr_a3_full']:
        cfg = VARIANTS[vname]
        steps, values = load_tb_scalars(vname, 'losses/l_ratr')
        if steps:
            n = max(1, len(steps) // 500)
            steps_sub = steps[::n]
            values_smooth = smooth(values[::n], weight=0.95)
            iters_k = [s / 1000 for s in steps_sub]
            ax.plot(iters_k, values_smooth, color=cfg['color'], linewidth=1.5, 
                    alpha=0.85, label=cfg['label'])
    
    ax.set_xlabel('Iteration (k)', fontsize=12)
    ax.set_ylabel('RATR Loss', fontsize=12)
    ax.set_title('RATR Loss Comparison — A2 (+RATR only) vs A3 (Full)', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', framealpha=0.9)
    ax.grid(True, linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    filepath = os.path.join(CHART_DIR, 'ratr_loss.png')
    fig.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  ✅ {filepath}")

def main():
    os.makedirs(CHART_DIR, exist_ok=True)
    
    print("📊 Generating ablation charts from TensorBoard data...")
    print()
    
    print("1/5 PSNR comparison...")
    plot_metric_comparison('psnr', 'PSNR (dB)', 'psnr_comparison.png')
    
    print("2/5 SSIM comparison...")
    plot_metric_comparison('ssim', 'SSIM', 'ssim_comparison.png', ylim=(0.86, 0.94))
    
    print("3/5 Generator losses...")
    plot_loss_curves()
    
    print("5/5 RATR loss comparison...")
    plot_ratr_loss()
    
    print(f"\n✅ All charts saved to {CHART_DIR}/")
    print("\nGenerated files:")
    for f in sorted(os.listdir(CHART_DIR)):
        if f.endswith('.png'):
            size_kb = os.path.getsize(os.path.join(CHART_DIR, f)) / 1024
            print(f"  📈 {f} ({size_kb:.0f}KB)")

if __name__ == '__main__':
    main()
