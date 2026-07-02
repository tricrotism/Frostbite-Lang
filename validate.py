#!/usr/bin/env python3
"""Checks every <code>.json catalog against en.json: valid JSON, no unknown keys, and every
{placeholder} preserved. Missing keys are only warnings — they fall back to English in the bot."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
TOKEN = re.compile(r"\{([A-Za-z0-9_]+)}")

en = json.loads((ROOT / "en.json").read_text(encoding="utf-8"))
failed = False

for path in sorted(ROOT.glob("*.json")):
    if path.name == "en.json":
        continue
    code = path.stem
    try:
        cat = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[{code}] INVALID JSON: {e}")
        failed = True
        continue

    errors = []
    warnings = []
    extra = sorted(set(cat) - set(en))
    if extra:
        errors.append(f"unknown keys (not in en.json): {extra}")
    missing = sorted(set(en) - set(cat))
    if missing:
        warnings.append(f"{len(missing)} key(s) missing (will fall back to English)")

    for key, value in cat.items():
        if key not in en:
            continue
        want = set(TOKEN.findall(en[key]))
        got = set(TOKEN.findall(value))
        if want != got:
            errors.append(f"{key}: placeholders {sorted(want)} -> {sorted(got)}")
        if not value.strip():
            errors.append(f"{key}: empty value")
        if len(en[key]) > 40 and value == en[key]:
            warnings.append(f"{key}: identical to English (untranslated?)")

    for w in warnings:
        print(f"[{code}] warning: {w}")
    if errors:
        failed = True
        print(f"[{code}] {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
    else:
        print(f"[{code}] OK ({len(cat)} keys)")

sys.exit(1 if failed else 0)
