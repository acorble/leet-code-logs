"""981. Time Based Key-Value Store のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
get は「timestamp 以下で最大の時刻」に対応する値を返す。無ければ空文字。
"""

import random


def test_example_1(solution):
    tm = solution.TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"      # 1 <= 3 なので bar
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"


def test_before_any_set(solution):
    """求める時刻より前に set が無ければ空文字。"""
    tm = solution.TimeMap()
    tm.set("foo", "bar", 10)
    assert tm.get("foo", 5) == ""
    assert tm.get("foo", 9) == ""
    assert tm.get("foo", 10) == "bar"


def test_unknown_key(solution):
    tm = solution.TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("baz", 1) == ""


def test_multiple_keys_are_independent(solution):
    tm = solution.TimeMap()
    tm.set("a", "a1", 1)
    tm.set("b", "b1", 2)
    tm.set("a", "a2", 3)
    assert tm.get("a", 2) == "a1"
    assert tm.get("b", 1) == ""
    assert tm.get("b", 5) == "b1"
    assert tm.get("a", 100) == "a2"


def test_overwrite_same_timestamp(solution):
    """同じ timestamp に上書きしたら、新しい値が返る。"""
    tm = solution.TimeMap()
    tm.set("k", "old", 5)
    tm.set("k", "new", 5)
    assert tm.get("k", 5) == "new"


def test_many_timestamps(solution):
    tm = solution.TimeMap()
    for i in range(1, 101):
        tm.set("k", f"v{i}", i * 2)
    assert tm.get("k", 1) == ""
    assert tm.get("k", 2) == "v1"
    assert tm.get("k", 3) == "v1"        # 2 以下で最大は 2
    assert tm.get("k", 200) == "v100"
    assert tm.get("k", 999) == "v100"


def test_random_against_brute_force(solution):
    """素朴な線形探索と突き合わせる。"""
    rng = random.Random(0)
    for _ in range(50):
        tm = solution.TimeMap()
        history = {}
        t = 0
        for _ in range(40):
            key = rng.choice(["a", "b", "c"])
            if rng.random() < 0.5:
                t += rng.randint(1, 3)          # timestamp は増加していく
                value = f"v{t}"
                tm.set(key, value, t)
                history.setdefault(key, []).append((t, value))
            else:
                query = rng.randint(0, t + 3)
                pairs = [v for ts, v in history.get(key, []) if ts <= query]
                expected = pairs[-1] if pairs else ""
                assert tm.get(key, query) == expected, (key, query, history)
