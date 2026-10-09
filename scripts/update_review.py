#!/usr/bin/env python3
"""解き直しの予定表 (REVIEW.md) を problems/ の復習ログから生成する。

各問題の README の「復習ログ」(日付と自力の記号) から次に解く日を計算し、
「次回やること」の箇条書きと合わせて一覧にする。間隔の決め方は _review.py を参照。

使い方:
    python scripts/update_review.py
    python scripts/update_review.py --today 2026-10-20   # 指定日時点で計算する
"""

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _review  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "problems"
OUT = ROOT / "REVIEW.md"
THIS_WEEK = 5  # 「今週やる」に出す件数


def collect(today: date) -> list:
    items = []
    for problem in sorted(p for c in PROBLEMS.iterdir() if c.is_dir() for p in c.iterdir() if p.is_dir()):
        readme = problem / "README.md"
        if not readme.exists():
            continue
        sched, steps = _review.load(readme)
        title = next(
            (ln[2:].strip() for ln in readme.read_text(encoding="utf-8").splitlines() if ln.startswith("# ")),
            problem.name,
        )
        overdue = (today - sched.due).days if sched.due else None
        items.append({
            "title": title,
            "link": problem.relative_to(ROOT).as_posix(),
            "sched": sched,
            "steps": steps,
            "overdue": overdue,
            # 期限切れどうしは「間隔に対してどれだけ遅れているか」で比べる。
            # 3 日間隔の 6 日超過は、1 か月間隔の 6 日超過より忘れている可能性が高い
            "urgency": overdue / sched.interval if overdue is not None else None,
        })
    return items


def row(item: dict) -> str:
    s = item["sched"]
    history = " → ".join(s.history) or "-"
    if item["overdue"] is None:
        status = "-"
    elif item["overdue"] > 0:
        status = f"**{item['overdue']} 日超過**"
    elif item["overdue"] == 0:
        status = "**今日**"
    else:
        status = f"あと {-item['overdue']} 日"
    steps = "<br>".join(item["steps"]) or ""
    return (
        f"| [{item['title']}]({item['link']}) | {s.last.isoformat() if s.last else '-'} | {history} "
        f"| {s.interval} 日 | {s.due.isoformat()} | {status} | {steps} |"
    )


def table(items: list) -> list:
    return [
        "| 問題 | 前回 | 自力の履歴 | 間隔 | 予定日 | 状態 | 次回やること |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        *(row(i) for i in items),
        "",
    ]


def main(argv: list | None = None) -> int:
    parser = argparse.ArgumentParser(description="REVIEW.md を生成する")
    parser.add_argument("--today", default="", help="この日付の時点で計算する (省略時は今日)")
    args = parser.parse_args(argv)
    today = date.fromisoformat(args.today) if args.today else date.today()

    items = collect(today)
    scheduled = [i for i in items if i["sched"].due]
    due = sorted((i for i in scheduled if i["overdue"] >= 0), key=lambda i: -i["urgency"])
    upcoming = sorted((i for i in scheduled if i["overdue"] < 0), key=lambda i: i["sched"].due)
    graduated = [i for i in items if i["sched"].graduated]

    intervals = " → ".join(f"{d} 日" for d in _review.INTERVALS)
    lines = [
        "# 解き直しの予定",
        "",
        "このファイルは `python scripts/update_review.py` で自動生成される。**手で編集しない。**",
        f"各問題の README の「復習ログ」と「次回やること」から作っている（{today.isoformat()} 時点）。",
        "",
        "## 間隔の決め方",
        "",
        f"何も見ずに解けるたびに間隔を広げる: {intervals} → 卒業",
        "",
        "| 自力 | 意味 | 次の間隔 |",
        "| --- | --- | --- |",
        "| ◎ | 何も見ずにすんなり解けた | 1 段広げる |",
        "| ○ | 何も見ずに解けたが時間がかかった | 据え置き（最低 1 週間） |",
        "| △ | ヒント・過去の解答・解説を見た | 3 日に戻す |",
        "| × | 解けなかった | 3 日に戻す |",
        "| ? | 記録なし | ○ と同じに扱う |",
        "",
        "同じ日の 2 回目以降（直後の書き直し）は数えない。",
        "期限切れは「間隔に対してどれだけ遅れているか」の割合が大きい順に並べている。",
        "",
        f"## 今週やる ({min(len(due), THIS_WEEK)})",
        "",
    ]
    lines += table(due[:THIS_WEEK]) if due else ["期限切れの問題はありません。", ""]
    if len(due) > THIS_WEEK:
        lines += [f"## 期限切れ（残り {len(due) - THIS_WEEK}）", "", *table(due[THIS_WEEK:])]
    lines += [f"## 今後の予定 ({len(upcoming)})", ""]
    lines += table(upcoming) if upcoming else ["予定はありません。", ""]
    if graduated:
        lines += [f"## 卒業 ({len(graduated)})", ""]
        lines += [f"- [{i['title']}]({i['link']})" for i in graduated] + [""]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"REVIEW.md を更新しました (期限切れ {len(due)} / 予定 {len(upcoming)} / 卒業 {len(graduated)})")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")  # Windows のコンソール (cp932) で落ちないように
    raise SystemExit(main())
