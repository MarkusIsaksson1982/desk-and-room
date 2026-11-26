"""Tests for the Desk & Room token system.

Run from the project root with:

    python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path
from types import ModuleType
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TOKENS_PATH = ROOT / "tokens.json"
CSS_PATH = ROOT / "styles" / "tokens.css"


def load_script(name: str) -> ModuleType:
    """Load a script from scripts/ without requiring it to be a package."""
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_tokens() -> dict[str, Any]:
    with TOKENS_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def px(value: str) -> float:
    """Parse a token value such as '15px' as a number of pixels."""
    return float(value.removesuffix("px"))


class ContrastTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contrast = load_script("contrast_table")
        cls.tokens = load_tokens()

    def test_black_and_white_contrast_is_21(self) -> None:
        self.assertAlmostEqual(
            self.contrast.contrast_ratio("#000000", "#FFFFFF"), 21.0, places=2
        )

    def test_known_pair_contrast(self) -> None:
        # #777777 on white is a commonly cited mid-grey pair, about 4.48:1.
        self.assertAlmostEqual(
            self.contrast.contrast_ratio("#777777", "#FFFFFF"), 4.48, places=2
        )

    def test_every_required_pair_passes(self) -> None:
        rows = list(self.contrast.required_pairs(self.tokens))
        self.assertTrue(rows, "No contrast pairs were produced.")
        for row in rows:
            with self.subTest(
                mode=row["mode"],
                foreground=row["foreground_role"],
                background=row["background_role"],
            ):
                self.assertGreaterEqual(
                    row["ratio"] + 1e-9,
                    row["required"],
                    msg=(
                        f"{row['mode']}: {row['foreground_role']} on "
                        f"{row['background_role']} is {row['ratio']:.2f}:1; "
                        f"requires {row['required']:.1f}:1"
                    ),
                )


class ModeScaleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tokens = load_tokens()

    def test_room_body_and_target_sizes(self) -> None:
        room = self.tokens["modes"]["room"]
        self.assertGreaterEqual(px(room["body_size"]), 28)
        self.assertGreaterEqual(px(room["min_target"]), 64)
        self.assertLessEqual(room["max_pupils_visible"], 6)

    def test_desk_body_size(self) -> None:
        desk = self.tokens["modes"]["desk"]
        self.assertGreaterEqual(px(desk["body_size"]), 13)
        self.assertLessEqual(px(desk["body_size"]), 16)


class StatusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tokens = load_tokens()
        cls.status = cls.tokens["status"]

    def test_every_status_has_a_distinct_shape_and_label(self) -> None:
        shapes = [entry["shape"] for entry in self.status.values()]
        labels = [entry["label"] for entry in self.status.values()]

        self.assertEqual(len(shapes), len(set(shapes)))
        self.assertEqual(len(labels), len(set(labels)))
        for name, entry in self.status.items():
            with self.subTest(status=name):
                self.assertTrue(entry["shape"].strip())
                self.assertTrue(entry["label"].strip())
                self.assertIn(entry["color"], self.tokens["color"])

    def test_every_status_pair_differs_by_shape(self) -> None:
        items = list(self.status.items())
        for left_index, (left_name, left) in enumerate(items):
            for right_name, right in items[left_index + 1 :]:
                with self.subTest(left=left_name, right=right_name):
                    self.assertNotEqual(left["shape"], right["shape"])


class GeneratedCssTests(unittest.TestCase):
    def test_tokens_css_is_up_to_date(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_tokens.py"), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_tokens_css_has_both_modes_and_reduced_motion(self) -> None:
        css = CSS_PATH.read_text(encoding="utf-8")
        self.assertIn(':root', css)
        self.assertIn('[data-mode="desk"]', css)
        self.assertIn('[data-mode="room"]', css)
        self.assertIn("@media (prefers-reduced-motion: reduce)", css)


if __name__ == "__main__":
    unittest.main()
