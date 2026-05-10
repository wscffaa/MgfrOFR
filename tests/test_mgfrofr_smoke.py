#!/usr/bin/env python3
"""Smoke test for MgfrOFR imports, registry entries, and option files."""

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

import mgfrofr.archs  # noqa: F401,E402
import mgfrofr.losses  # noqa: F401,E402
import mgfrofr.models  # noqa: F401,E402
from basicsr.utils.registry import ARCH_REGISTRY, LOSS_REGISTRY, MODEL_REGISTRY  # noqa: E402


def main() -> None:
    assert ARCH_REGISTRY.get("MgfrOFR") is not None
    assert MODEL_REGISTRY.get("MGFROFRModel") is not None
    assert LOSS_REGISTRY.get("RATRLoss") is not None

    option_files = sorted((REPO_ROOT / "options").rglob("*.yml"))
    assert option_files, "no option files found"
    for option_file in option_files:
        data = yaml.safe_load(option_file.read_text())
        assert data.get("name"), option_file
        assert data.get("model_type"), option_file
        assert data.get("network_g", {}).get("type"), option_file

    print("MgfrOFR import, registry, and config smoke test passed")


if __name__ == "__main__":
    main()
