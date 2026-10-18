#!/usr/bin/env python3
"""解き直しの予定を、カレンダーに登録する形 (JSON) で出力する。

REVIEW.md と同じ計算 (update_review.collect) で予定日を出し、
タイトル・説明・時間・通知を毎回同じ形式にそろえる。カレンダーへの登録自体はしない。

形式:
  - 予定日の 07:00–09:00
  - 通知は前日 23:00 (480 分前) と当日 07:00 (0 分前)
  - タイトル「LeetCode 解き直し: <番号>. <タイトル>」

使い方:
    python scripts/review_events.py                        # 今日から 7 日以内に予定日が来るもの
    python scripts/review_events.py --days 14              # 14 日以内
    python scripts/review_events.py --assign 543=2026-10-23 --assign 125=2026-10-24
                                                           # 期限切れの問題などを指定日に入れる
出力の "overdue" には、期限切れで日付が決まっていない問題が入る (--assign で日付を決める)。
"""

import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import update_review  # noqa: E402

ROOT = update_review.ROOT
START, END = "07:00:00", "09:00:00"
REMINDERS = [{"method": "popup", "minutes": 480}, {"method": "popup", "minutes": 0}]
URL_RE = re.compile(r"https://leetcode\.com/problems/[\w-]+/")


def number_of(item: dict) -> int:
    return int(item["title"].split(".", 1)[0])


def url_of(item: dict) -> str:
    solution = ROOT / item["link"] / "solution.py"
    m = URL_RE.search(solution.read_text(encoding="utf-8")) if solution.exists() else None
    return m.group(0) if m else ""


def event(item: dict, day: date) -> dict:
    lines = []
    if item["steps"]:
        lines += ["次回やること:", *(f"- {s.replace('`', '')}" for s in item["steps"]), ""]
    if url := url_of(item):
        lines.append(f"問題: {url}")
    lines.append(f"記録: leet-code-logs/{item['link']}")
    return {
        "number": number_of(item),
        "due": item["sched"].due.isoformat(),
        "summary": f"LeetCode 解き直し: {item['title']}",
        "startTime": f"{day.isoformat()}T{START}",
        "endTime": f"{day.isoformat()}T{END}",
        "description": "\n".join(lines),
        "overrideReminders": REMINDERS,
    }


def main(argv: list | None = None) -> int:
    parser = argparse.ArgumentParser(description="解き直しの予定をカレンダー登録用の JSON で出す")
    parser.add_argument("--today", default="", help="この日付の時点で計算する (省略時は今日)")
    parser.add_argument("--days", type=int, default=7, help="今日から何日先までの予定を出すか (既定 7)")
    parser.add_argument("--assign", action="append", default=[], metavar="番号=YYYY-MM-DD",
                        help="この問題をこの日に入れる (期限切れの問題など。複数指定可)")
    args = parser.parse_args(argv)
    today = date.fromisoformat(args.today) if args.today else date.today()

    items = [i for i in update_review.collect(today) if i["sched"].due]
    by_number = {number_of(i): i for i in items}

    assigned = {}
    for a in args.assign:
        num, _, day = a.partition("=")
        if int(num) not in by_number:
            parser.error(f"{num} は予定のある問題ではありません")
        assigned[int(num)] = date.fromisoformat(day)

    horizon = today + timedelta(days=args.days)
    events, overdue = [], []
    for i in sorted(items, key=lambda i: i["sched"].due):
        num, due = number_of(i), i["sched"].due
        if num in assigned:
            events.append(event(i, assigned[num]))
        elif today <= due <= horizon:
            events.append(event(i, due))
        elif due < today:
            overdue.append({"number": num, "title": i["title"], "due": due.isoformat(),
                            "overdue_days": (today - due).days})
    events.sort(key=lambda e: e["startTime"])
    overdue.sort(key=lambda o: -o["overdue_days"])

    print(json.dumps({"today": today.isoformat(), "events": events, "overdue": overdue},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    raise SystemExit(main())
