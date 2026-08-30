#!/usr/bin/env python3
"""新しい問題用のディレクトリと雛形を作る。

使い方:
    python scripts/new_problem.py 1 "Two Sum" --category array --difficulty easy
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
PROBLEMS = ROOT / "problems"


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower())
    return slug.strip("-")


def main() -> int:
    parser = argparse.ArgumentParser(description="LeetCode の問題ディレクトリを作成する")
    parser.add_argument("number", type=int, help="問題番号 (例: 1)")
    parser.add_argument("title", help="問題タイトル (例: 'Two Sum')")
    parser.add_argument("-c", "--category", default="misc", help="カテゴリ (problems/ 配下のディレクトリ名)")
    parser.add_argument("-d", "--difficulty", default="", choices=["", "easy", "medium", "hard"], help="難易度")
    parser.add_argument("-u", "--url", default="", help="問題 URL (省略時はスラッグから生成)")
    args = parser.parse_args()

    slug = slugify(args.title)
    number = f"{args.number:04d}"
    dir_name = f"{number}-{slug}"
    category_dir = PROBLEMS / args.category
    target = category_dir / dir_name

    if not category_dir.exists():
        existing = sorted(p.name for p in PROBLEMS.iterdir() if p.is_dir())
        print(f"カテゴリ '{args.category}' がありません。既存: {', '.join(existing)}", file=sys.stderr)
        print("新しく作る場合は mkdir problems/<category> を実行してください。", file=sys.stderr)
        return 1
    if target.exists():
        print(f"すでに存在します: {target.relative_to(ROOT)}", file=sys.stderr)
        return 1

    fields = {
        "number": number.lstrip("0") or "0",
        "title": args.title,
        "url": args.url or f"https://leetcode.com/problems/{slug}/",
        "difficulty": args.difficulty or "?",
        "category": args.category,
        "date": date.today().isoformat(),
    }

    target.mkdir(parents=True)
    files = {
        "README.md": "README.md",
        "solution.py": "solution.py",
        "test_solution.py": f"test_{number}_{slug.replace('-', '_')}.py",
    }
    for template_name, out_name in files.items():
        content = (TEMPLATES / template_name).read_text(encoding="utf-8").format(**fields)
        (target / out_name).write_text(content, encoding="utf-8")

    print(f"作成しました: {target.relative_to(ROOT)}")
    for out_name in files.values():
        print(f"  - {out_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
