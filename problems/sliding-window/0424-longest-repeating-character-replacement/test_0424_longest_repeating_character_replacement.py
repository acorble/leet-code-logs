"""424. Longest Repeating Character Replacement のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
k 個まで文字を置き換えてよいとき、同じ文字だけにできる最長の部分文字列の長さを返す。
"""

import random
from collections import Counter


def longest(solution, s, k):
    return solution.Solution().characterReplacement(s, k)


def brute_force(s, k):
    """全ての部分文字列を試す（正解の基準）。

    その部分文字列の中で最頻の文字以外を全部置き換えるので、
    (長さ - 最頻の出現数) <= k なら成立する。
    """
    best = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            window = s[i:j + 1]
            if len(window) - max(Counter(window).values()) <= k:
                best = max(best, len(window))
    return best


def test_example_1(solution):
    """A を B に 1 つ替えれば BBBB。"""
    assert longest(solution, "ABAB", 2) == 4


def test_example_2(solution):
    """AABABBA の真ん中 4 文字。"""
    assert longest(solution, "AABABBA", 1) == 4


def test_single(solution):
    assert longest(solution, "A", 0) == 1


def test_no_replacement_allowed(solution):
    """k=0 なら、単純に同じ文字が続く最長。"""
    assert longest(solution, "AABBBCC", 0) == 3


def test_all_same(solution):
    assert longest(solution, "AAAA", 2) == 4


def test_k_covers_everything(solution):
    """k が十分大きければ全体を 1 文字にできる。"""
    assert longest(solution, "ABCDE", 4) == 5
    assert longest(solution, "ABCDE", 10) == 5


def test_random_against_brute_force(solution):
    rng = random.Random(0)
    for alphabet in ("AB", "ABC", "ABCD"):
        for _ in range(200):
            s = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 16)))
            k = rng.randint(0, 4)
            assert longest(solution, s, k) == brute_force(s, k), (s, k)
