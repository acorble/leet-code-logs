#!/usr/bin/env python3
"""problems/ を走査して README.md の一覧テーブルを更新する。

各問題の README.md 冒頭のメタ情報 (難易度・解いた日・URL) を読み取り、
README.md 内の <!-- INDEX:START --> ... <!-- INDEX:END --> を書き換える。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "problems"
README = ROOT / "README.md"
START = "<!-- INDEX:START -->"
END = "<!-- INDEX:END -->"


def meta(readme: Path) -> dict:
    text = readme.read_text(encoding="utf-8") if readme.exists() else ""
    out = {}
    for key, label in (("url", "URL"), ("difficulty", "難易度"), ("date", "解いた日")):
        m = re.search(rf"^- {label}: (.*)$", text, re.MULTILINE)
        out[key] = m.group(1).strip() if m else ""
    m = re.search(r"^# (.*)$", text, re.MULTILINE)
    out["title"] = m.group(1).strip() if m else ""
    return out


def main() -> int:
    rows = []
    for category_dir in sorted(p for p in PROBLEMS.iterdir() if p.is_dir()):
        for problem_dir in sorted(p for p in category_dir.iterdir() if p.is_dir()):
            info = meta(problem_dir / "README.md")
            number = problem_dir.name.split("-")[0]
            title = info["title"] or problem_dir.name
            link = f"[{title}]({problem_dir.relative_to(ROOT)})"
            rows.append(
                f"| {number.lstrip('0') or '0'} | {link} | {info['difficulty'] or '-'} "
                f"| {category_dir.name} | {info['date'] or '-'} |"
            )

    table = [
        f"合計 {len(rows)} 問",
        "",
        "| # | 問題 | 難易度 | カテゴリ | 解いた日 |",
        "| --- | --- | --- | --- | --- |",
        *rows,
    ] if rows else ["まだ問題がありません。"]

    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print(f"README.md に {START} / {END} のマーカーがありません。", file=sys.stderr)
        return 1
    new = re.sub(
        rf"{re.escape(START)}.*?{re.escape(END)}",
        START + "\n\n" + "\n".join(table) + "\n\n" + END,
        text,
        flags=re.DOTALL,
    )
    README.write_text(new, encoding="utf-8")
    print(f"README.md を更新しました ({len(rows)} 問)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
