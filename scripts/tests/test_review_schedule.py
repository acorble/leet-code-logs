"""_review.py (解き直しの間隔の計算) のテスト。"""

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _review  # noqa: E402


def rows(*pairs):
    return [{"回": str(i + 1), "日付": d, "自力": m} for i, (d, m) in enumerate(pairs)]


def test_first_solve_without_help_waits_a_week():
    s = _review.schedule(rows(("2026-10-01", "◎")))
    assert s.interval == 7
    assert s.due == date(2026, 10, 8)


def test_double_check_widens_each_time():
    s = _review.schedule(rows(("2026-01-01", "◎"), ("2026-01-08", "◎"), ("2026-01-22", "◎")))
    assert s.interval == 30


def test_looked_at_answer_resets_to_three_days():
    s = _review.schedule(rows(("2026-09-02", "◎"), ("2026-10-09", "△")))
    assert s.interval == 3
    assert s.due == date(2026, 10, 12)


def test_slow_solve_keeps_interval_but_at_least_a_week():
    assert _review.schedule(rows(("2026-01-01", "○"))).interval == 7
    s = _review.schedule(rows(("2026-01-01", "◎"), ("2026-01-08", "◎"), ("2026-01-22", "○")))
    assert s.interval == 14


def test_unknown_is_treated_like_slow_solve():
    assert _review.schedule(rows(("2026-01-01", "?"))).interval == 7


def test_same_day_rework_is_not_counted():
    s = _review.schedule(rows(("2026-08-30", "○"), ("2026-08-30", "◎")))
    assert s.history == ["○"]
    assert s.interval == 7


def test_graduates_after_success_at_last_stage():
    days = ["2026-01-01", "2026-01-08", "2026-01-22", "2026-02-21", "2026-04-22", "2026-06-21"]
    s = _review.schedule(rows(*[(d, "◎") for d in days]))
    assert s.graduated
    assert s.due is None


def test_giveup_without_mark_counts_as_failure():
    s = _review.schedule([{"回": "1", "日付": "2026-01-01", "結果": "giveup"}])
    assert s.history == ["×"]
    assert s.interval == 3


def test_parse_attempts_and_next_steps():
    text = """# 1. Two Sum

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 自力 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-07-11 | AC | ○ | - | [solution.py](solution.py) | |

<!-- ATTEMPTS:END -->

## 次回やること

<!-- - [ ] コメント内は無視 -->

- [ ] 1 パスで書く
- [x] 済んだもの
- 印なしも拾う

## 問題の要約
"""
    attempts = _review.parse_attempts(text)
    assert attempts[0]["自力"] == "○"
    assert _review.parse_next_steps(text) == ["1 パスで書く", "印なしも拾う"]
