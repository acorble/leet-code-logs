"""567. Permutation in String のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
s1 の並べ替えのどれかが s2 の連続した部分文字列になっているかを判定する。
"""

import random
from collections import Counter


def check(solution, s1, s2):
    return solution.Solution().checkInclusion(s1, s2)


def brute_force(s1, s2):
    """s2 の全ての長さ len(s1) の窓を試す（正解の基準）。"""
    need = Counter(s1)
    n = len(s1)
    return any(Counter(s2[i:i + n]) == need for i in range(len(s2) - n + 1))


def test_example_1(solution):
    """ba が s2 に含まれる。"""
    assert check(solution, "ab", "eidbaooo") is True


def test_example_2(solution):
    assert check(solution, "ab", "eidboaoo") is False


def test_exact_match(solution):
    assert check(solution, "abc", "cba") is True


def test_s1_longer_than_s2(solution):
    assert check(solution, "abcd", "abc") is False


def test_single_char(solution):
    assert check(solution, "a", "a") is True
    assert check(solution, "a", "b") is False


def test_repeated_chars(solution):
    """個数まで一致する必要がある。"""
    assert check(solution, "aab", "abab") is True
    assert check(solution, "aab", "abba") is False


def test_match_at_the_end(solution):
    assert check(solution, "ab", "oooba") is True


def test_unrelated_char_resets_window(solution):
    """s1 に無い文字をまたいだ窓は成立しない。"""
    assert check(solution, "ab", "axb") is False


def test_random_against_brute_force(solution):
    rng = random.Random(0)
    for alphabet in ("ab", "abc", "abcd"):
        for _ in range(300):
            s1 = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 5)))
            s2 = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 20)))
            assert check(solution, s1, s2) == brute_force(s1, s2), (s1, s2)
