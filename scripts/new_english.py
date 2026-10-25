#!/usr/bin/env python3
"""英語で話した記録（mock interview / 一人での説明練習）の雛形を作る。

problems/<category>/<dir>/english/<日付>-<mock|solo>.md を作り、
問題 README の「## 英語での説明」にリンクを足す。

mock は「解いた 1 回」として数えるので、先に new_attempt.py（初回なら new_problem.py）で
復習ログに今日の行を作っておく。mock のときはその行のメモ欄にも記録へのリンクを足す。
一人練習は解いた回として数えないので、復習ログには触らない。

使い方:
    python scripts/new_english.py 84 mock --interviewer Shin
    python scripts/new_english.py 84 solo
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _open_editor import open_in_editor  # noqa: E402
from new_attempt import END, ROOT, START, find_problem  # noqa: E402

TEMPLATES = ROOT / "templates"
HEADING = "## 英語での説明"
LABELS = {"mock": "mock", "solo": "一人練習"}


def record_path(english_dir: Path, day: str, kind: str) -> Path:
    """同じ日に同じ種類を複数回やった場合は -2, -3 と連番を付ける。"""
    candidate = english_dir / f"{day}-{kind}.md"
    n = 2
    while candidate.exists():
        candidate = english_dir / f"{day}-{kind}-{n}.md"
        n += 1
    return candidate


def add_link(readme: Path, line: str) -> None:
    """「## 英語での説明」の末尾にリンクの行を足す。節が無い古い README には作る。"""
    text = readme.read_text(encoding="utf-8")
    start = text.find(HEADING)
    if start == -1:
        # 新しい雛形と同じく「問題の要約」の直前に置く。無ければ末尾
        anchor = text.find("\n## 問題の要約")
        section = f"\n{HEADING}\n\n{line}\n"
        if anchor == -1:
            text = text.rstrip() + "\n" + section
        else:
            text = text[: anchor + 1] + section.lstrip("\n") + "\n" + text[anchor + 1 :]
        readme.write_text(text, encoding="utf-8")
        return

    end = text.find("\n## ", start + len(HEADING))
    end = len(text) if end == -1 else end
    section = text[start:end].rstrip()
    # 最初の 1 行は見出しや説明のコメントと空行で離す。2 行目からは前の行に続ける
    sep = "\n" if re.search(r"^- ", section, re.MULTILINE) else "\n\n"
    section += f"{sep}{line}\n"
    readme.write_text(text[:start] + section + text[end:], encoding="utf-8")


def link_attempt(readme: Path, day: str, link: str) -> bool:
    """復習ログの最新の行が今日の回なら、そのメモ欄に記録へのリンクを足す。"""
    text = readme.read_text(encoding="utf-8")
    m = re.search(rf"{re.escape(START)}(.*?){re.escape(END)}", text, re.DOTALL)
    if not m:
        return False
    rows = [ln for ln in m.group(1).splitlines() if re.match(r"^\|\s*\d+\s*\|", ln)]
    if not rows:
        return False
    last = rows[-1]
    cells = last.strip().strip("|").split("|")
    if cells[1].strip() != day:
        return False
    note = cells[-1].strip()
    cells[-1] = f" {note} {link} " if note else f" {link} "
    new_last = "|" + "|".join(cells) + "|"
    block = m.group(1).replace(last, new_last)
    text = text[: m.start(1)] + block + text[m.end(1) :]
    readme.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="英語で話した記録の雛形を作る")
    parser.add_argument("problem", help="問題番号 (例: 84)、スラッグの一部、または問題ディレクトリのパス")
    parser.add_argument("kind", choices=["mock", "solo"], help="mock: 人との mock interview / solo: 一人での説明練習")
    parser.add_argument("-i", "--interviewer", default="", help="面接官役の名前 (mock のみ)")
    parser.add_argument("--date", default="", help="録音した日 (省略時は今日。例: 2026-10-30)")
    parser.add_argument("--no-open", action="store_true", help="記録をエディタで開かない")
    args = parser.parse_args()

    problem = find_problem(args.problem)
    readme = problem / "README.md"
    title = re.search(r"^# (\d+)\. (.*)$", readme.read_text(encoding="utf-8"), re.MULTILINE)
    if not title:
        sys.exit(f"README の 1 行目から番号とタイトルを読めません: {readme.relative_to(ROOT)}")
    day = args.date or date.today().isoformat()

    english = problem / "english"
    english.mkdir(exist_ok=True)
    dest = record_path(english, day, args.kind)
    fields = {
        "number": title.group(1),
        "title": title.group(2),
        "date": day,
        "interviewer": args.interviewer or "-",
    }
    content = (TEMPLATES / f"english-{args.kind}.md").read_text(encoding="utf-8").format(**fields)
    dest.write_text(content, encoding="utf-8")
    rel = dest.relative_to(problem).as_posix()

    who = f"（面接官: {args.interviewer}）" if args.interviewer else ""
    add_link(readme, f"- {day} {LABELS[args.kind]}{who}: [{rel}]({rel})")

    print(f"作成しました: {dest.relative_to(ROOT)}")
    print(f"  README の「{HEADING}」にリンクを足しました")
    if args.kind == "mock":
        if link_attempt(readme, day, f"[mock 記録]({rel})"):
            print("  復習ログの今日の回のメモ欄にもリンクを足しました")
        else:
            print(
                f"  (復習ログに {day} の回が最新の行として見つからないので、メモ欄にはリンクしていません。"
                "先に new_attempt.py を実行したか確認してください)",
                file=sys.stderr,
            )
    if not args.no_open:
        open_in_editor(dest)
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")  # Windows のコンソール (cp932) で落ちないように
    raise SystemExit(main())
