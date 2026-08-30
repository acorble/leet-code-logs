#!/usr/bin/env python3
"""NeetCode 150 の進捗 (PROGRESS.md) を problems/ の実態から生成する。

チェックは手で付けない。problems/ に問題ディレクトリがあれば「解いた」とみなす。
問題リストは data/neetcode150.tsv。
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "problems"
DATA = ROOT / "data" / "neetcode150.tsv"
OUT = ROOT / "PROGRESS.md"

# problems/ に用意してあるカテゴリ = いま学習対象にしているセクション
ACTIVE = {p.name for p in PROBLEMS.iterdir() if p.is_dir()}


def solved_problems() -> dict:
    """問題番号 -> (ディレクトリ, 解いた回数, 最後に解いた日)。"""
    found = {}
    for problem in sorted(p for c in PROBLEMS.iterdir() if c.is_dir() for p in c.iterdir() if p.is_dir()):
        m = re.match(r"^(\d{4})-", problem.name)
        if not m:
            continue
        readme = problem / "README.md"
        text = readme.read_text(encoding="utf-8") if readme.exists() else ""
        block = re.search(r"<!-- ATTEMPTS:START -->(.*?)<!-- ATTEMPTS:END -->", text, re.DOTALL)
        dates = re.findall(r"^\|\s*\d+\s*\|\s*([^|]*?)\s*\|", block.group(1), re.MULTILINE) if block else []
        found[int(m.group(1))] = (problem, len(dates) or 1, dates[-1] if dates else "-")
    return found


def load_list() -> list:
    rows = []
    for line in DATA.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        section, category, number, title, difficulty, *rest = line.split("\t")
        rows.append({
            "section": section,
            "category": category,
            "number": int(number),
            "title": title,
            "difficulty": difficulty,
            "premium": (rest[0].strip() if rest else "") == "premium",
        })
    return rows


def bar(done: int, total: int, width: int = 20) -> str:
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def main() -> int:
    solved = solved_problems()
    rows = load_list()

    sections = []
    for row in rows:
        if not sections or sections[-1][0] != row["section"]:
            sections.append((row["section"], []))
        sections[-1][1].append(row)

    done_total = sum(1 for r in rows if r["number"] in solved)
    lines = [
        "# NeetCode 150 の進捗",
        "",
        "このファイルは `python scripts/update_progress.py` で自動生成される。**手で編集しない。**",
        "`problems/` に問題ディレクトリがあるものを「解いた」として集計している。",
        "",
        f"## 全体: {done_total} / {len(rows)}",
        "",
        f"`{bar(done_total, len(rows), 40)}` {done_total / len(rows) * 100:.1f}%",
        "",
        "| セクション | 進捗 | | 学習対象 |",
        "| --- | --- | --- | --- |",
    ]
    for name, items in sections:
        done = sum(1 for r in items if r["number"] in solved)
        active = "◯" if items[0]["category"] in ACTIVE else "";
        lines.append(f"| {name} | {done} / {len(items)} | `{bar(done, len(items), 12)}` | {active} |")

    lines += [
        "",
        "「学習対象」の ◯ は `problems/` にカテゴリを用意してあるセクション。",
        "範囲を広げるときは `mkdir problems/<category>` して、",
        "`data/neetcode150.tsv` の 2 列目にそのカテゴリ名を入れる。",
        "",
    ]

    for name, items in sections:
        done = sum(1 for r in items if r["number"] in solved)
        lines += [
            f"## {name} — {done} / {len(items)}",
            "",
            "| | # | 問題 | 難易度 | 回数 | 最後に解いた日 |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for r in items:
            title = r["title"] + (" 🔒" if r["premium"] else "")
            if r["number"] in solved:
                problem, count, last = solved[r["number"]]
                link = f"[{title}]({problem.relative_to(ROOT)})"
                lines.append(f"| ✅ | {r['number']} | {link} | {r['difficulty']} | {count} | {last} |")
            else:
                lines.append(f"| ⬜ | {r['number']} | {title} | {r['difficulty']} | - | - |")
        lines.append("")

    lines += ["🔒 は LeetCode Premium 限定の問題。", ""]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"PROGRESS.md を更新しました ({done_total} / {len(rows)} 問)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
