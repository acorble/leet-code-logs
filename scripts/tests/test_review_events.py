"""review_events.py (解き直しの予定をカレンダー登録用に出す) のテスト。"""

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _review  # noqa: E402
import review_events  # noqa: E402


def item(steps=None):
    return {
        "title": "739. Daily Temperatures",
        "link": "problems/stack/0739-daily-temperatures",
        "sched": _review.schedule([{"回": "1", "日付": "2026-10-15", "自力": "○"}]),
        "steps": steps or [],
    }


def test_event_is_7_to_9_on_the_given_day():
    e = review_events.event(item(), date(2026, 10, 22))
    assert e["startTime"] == "2026-10-22T07:00:00"
    assert e["endTime"] == "2026-10-22T09:00:00"
    assert e["summary"] == "LeetCode 解き直し: 739. Daily Temperatures"


def test_reminders_are_previous_night_23_and_7am():
    e = review_events.event(item(), date(2026, 10, 22))
    assert sorted(r["minutes"] for r in e["overrideReminders"]) == [0, 480]


def test_description_lists_next_steps_without_backticks():
    e = review_events.event(item(["提出前に `print` を消す"]), date(2026, 10, 22))
    assert "- 提出前に print を消す" in e["description"]
    assert "https://leetcode.com/problems/daily-temperatures/" in e["description"]
