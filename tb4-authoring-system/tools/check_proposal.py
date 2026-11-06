#!/usr/bin/env python3
"""Local preflight for a proposal markdown file.

Enforces the limits this PDF states in text. It does not judge difficulty,
novelty, or the six review criteria.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("proposal", type=Path)
    args = parser.parse_args()
    text = args.proposal.read_text(encoding="utf-8")
    failures: list[str] = []
    if "REPLACE_ME" in text:
        failures.append("proposal still contains REPLACE_ME")
    if len(text) >= 2000:
        failures.append(
            f"character count is {len(text)}; p.5 requires under 2000 characters"
        )
    if "\n#" in "\n" + text:
        failures.append(
            "markdown heading found; the form asks for two or three paragraphs, "
            "and p.8 treats tidy headings as unreviewed LLM synthesis"
        )
    lowered = text.lower()
    for phrase in ("think step by step", "you are an expert"):
        if phrase in lowered:
            failures.append(f"steering phrase {phrase!r} is present")
    paragraphs = [p for p in text.strip().split("\n\n") if p.strip()]
    if len(paragraphs) < 2 or len(paragraphs) > 3:
        failures.append(
            f"{len(paragraphs)} paragraphs after splitting on blank lines; "
            "the form target is two or three"
        )
    print(f"characters {len(text)}")
    print(f"paragraphs {len(paragraphs)}")
    if failures:
        print("FAIL")
        for item in failures:
            print(f"- {item}")
        return 1
    print("PASS")
    print("Manual: confirm all six section 3.3 topics are actually covered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
