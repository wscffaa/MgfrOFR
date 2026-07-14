#!/usr/bin/env python3
"""Build a CVPR-style supplementary comparison video for MgfrOFR.

Usage:
    python make_supplementary_video.py --config video_config.json --out supplementary_video_s1.mp4

Config example (synthetic clips with GT):
{
  "fps": 24,
  "codec": "mp4v",
  "panels": ["Input", "MambaOFR (A0)", "MgfrOFR (F1)", "GT"],
  "clips": [
    {
      "id": "clip_000",
      "frames": [0, 30],
      "sources": [
        "local_frames/REDS_synthetic/000/LQ/{idx:08d}.png",
        "local_frames/REDS_synthetic/000/A0/{idx:08d}_mgfrofr_a0_synthetic.png",
        "local_frames/REDS_synthetic/000/F1/{idx:08d}_mgfrofr_f1_synthetic.png",
        "local_frames/REDS_synthetic/000/GT/{idx:08d}.png"
      ]
    }
  ]
}

The script concatenates clips with a title card inserted at the start of each clip.
Output resolution is kept small (2x2 grid of 256x256 frames -> 512x512) so the
final MP4 stays well below typical 100 MB supplementary limits.
"""

import argparse
import json
import sys
from pathlib import Path

import cv2
import numpy as np


def put_label(img, label, pos=(8, 24), font_scale=0.55, thickness=1):
    """Draw a small black-outline white label on the top-left of a panel."""
    font = cv2.FONT_HERSHEY_SIMPLEX
    x, y = pos
    cv2.putText(img, label, (x + 1, y + 1), font, font_scale, (0, 0, 0), thickness + 1, cv2.LINE_AA)
    cv2.putText(img, label, (x, y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)
    return img


def make_tile(images, labels, target_size=None, pad=2):
    """Stack four images into a 2x2 grid with labels.

    If target_size is given as [h, w], all panels are resized to that size.
    Otherwise the size of the first panel is used.
    """
    if target_size is None:
        h, w = images[0].shape[:2]
    else:
        h, w = target_size
    canvas = np.full((2 * h + pad, 2 * w + pad, 3), 30, dtype=np.uint8)
    positions = [(0, 0), (0, w + pad), (h + pad, 0), (h + pad, w + pad)]
    for (y, x), img, label in zip(positions, images, labels):
        if img.shape[:2] != (h, w):
            img = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)
        img = put_label(img.copy(), label)
        canvas[y : y + h, x : x + w] = img
    return canvas


def add_clip_title(frame, title, font_scale=0.6):
    """Overlay clip title at bottom-center."""
    h, w = frame.shape[:2]
    text_size = cv2.getTextSize(title, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)[0]
    x = (w - text_size[0]) // 2
    y = h - 10
    cv2.putText(frame, title, (x + 1, y + 1), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(frame, title, (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), 2, cv2.LINE_AA)
    return frame


def build_video(config_path, out_path):
    cfg = json.loads(Path(config_path).read_text(encoding="utf-8"))
    fps = cfg.get("fps", 24)
    codec = cfg.get("codec", "mp4v")
    labels = cfg["panels"]
    clips = cfg["clips"]
    target_size = cfg.get("target_size")  # [h, w], e.g. [368, 640]

    writer = None
    out_h = out_w = None

    for clip in clips:
        start, end = clip["frames"]
        sources = clip["sources"]
        clip_title = clip.get("title", clip.get("id", ""))
        # Title card: 1 second black screen with white text
        if writer is None:
            # peek first frame to know canvas size
            sample = cv2.imread(sources[0].format(idx=start))
            if sample is None:
                raise FileNotFoundError(f"Cannot read sample frame: {sources[0].format(idx=start)}")
            tile = make_tile([sample] * 4, labels, target_size=target_size)
            out_h, out_w = tile.shape[:2]
            fourcc = cv2.VideoWriter_fourcc(*codec)
            writer = cv2.VideoWriter(str(out_path), fourcc, fps, (out_w, out_h))
            if not writer.isOpened():
                raise RuntimeError(f"Failed to open video writer for {out_path}; try codec 'avc1' or 'mp4v'.")

        title_card = np.full((out_h, out_w, 3), 15, dtype=np.uint8)
        cv2.putText(title_card, clip_title, ((out_w - cv2.getTextSize(clip_title, cv2.FONT_HERSHEY_SIMPLEX, 0.9, 2)[0][0]) // 2, out_h // 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (220, 220, 220), 2, cv2.LINE_AA)
        cv2.putText(title_card, "REDS synthetic old-film restoration", ((out_w - cv2.getTextSize("REDS synthetic old-film restoration", cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0][0]) // 2, out_h // 2 + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (180, 180, 180), 1, cv2.LINE_AA)
        for _ in range(fps):
            writer.write(title_card)

        for idx in range(start, end):
            images = []
            for src in sources:
                path = src.format(idx=idx)
                img = cv2.imread(path)
                if img is None:
                    raise FileNotFoundError(f"Missing frame: {path}")
                images.append(img)
            tile = make_tile(images, labels, target_size=target_size)
            tile = add_clip_title(tile, clip_title)
            writer.write(tile)

    if writer is not None:
        writer.release()
    print(f"Wrote {out_path} ({out_w}x{out_h} @ {fps} fps)")


def main():
    parser = argparse.ArgumentParser(description="Build supplementary comparison video for MgfrOFR")
    parser.add_argument("--config", required=True, help="JSON config path")
    parser.add_argument("--out", required=True, help="Output MP4 path")
    args = parser.parse_args()
    build_video(args.config, args.out)


if __name__ == "__main__":
    main()
