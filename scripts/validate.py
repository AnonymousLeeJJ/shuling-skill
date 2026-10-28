# -*- coding: utf-8 -*-
"""Validate a distilled advisor skill folder.

Usage: python scripts/validate.py <skill-dir>
Checks: SKILL.md exists, frontmatter fields, required sections, line budget.
"""
import re, sys, pathlib

REQUIRED_SECTIONS = ["核心方法论", "工作流程", "检查清单", "常见误区", "诚实边界"]


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate.py <skill-dir>")
        sys.exit(1)
    root = pathlib.Path(sys.argv[1])
    skill = root / "SKILL.md"
    errors, warnings = [], []

    if not skill.exists():
        print(f"FAIL: {skill} not found")
        sys.exit(1)

    text = skill.read_text(encoding="utf-8")
    lines = text.splitlines()

    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append("missing YAML frontmatter")
    else:
        fm = m.group(1)
        for field in ("name:", "description:"):
            if field not in fm:
                errors.append(f"frontmatter missing {field}")

    for sec in REQUIRED_SECTIONS:
        if sec not in text:
            errors.append(f"missing section: {sec}")

    if len(lines) > 400:
        errors.append(f"main file too long: {len(lines)} lines (limit 400)")
    elif len(lines) > 300:
        warnings.append(f"main file {len(lines)} lines, consider moving detail to references/")

    for w in warnings:
        print("WARN:", w)
    if errors:
        for e in errors:
            print("FAIL:", e)
        sys.exit(1)
    print(f"OK: {root} ({len(lines)} lines, all required sections present)")


if __name__ == "__main__":
    main()
