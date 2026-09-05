"""3. Longest Substring Without Repeating Characters のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
"""

import random
import string


def length_of(solution, s):
    return solution.Solution().lengthOfLongestSubstring(s)


def brute_force(s):
    """全ての部分文字列を試す（正解の基準）。"""
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best


def test_example_1(solution):
    """abc の 3。"""
    assert length_of(solution, "abcabcbb") == 3


def test_example_2(solution):
    """すべて同じ文字。"""
    assert length_of(solution, "bbbbb") == 1


def test_example_3(solution):
    """wke の 3。pwke ではない（部分列ではなく連続した部分文字列）。"""
    assert length_of(solution, "pwwkew") == 3


def test_empty(solution):
    assert length_of(solution, "") == 0


def test_single(solution):
    assert length_of(solution, "a") == 1


def test_all_unique(solution):
    assert length_of(solution, "abcdef") == 6


def test_duplicate_outside_window(solution):
    """左端より前にある重複は、窓の中には無いので縮めなくてよい。"""
    assert length_of(solution, "abba") == 2


def test_spaces_and_symbols(solution):
    assert length_of(solution, "a b!a b!") == 4


def test_random_against_brute_force(solution):
    """小さいアルファベットで衝突を起こしやすくして総当たりと比較。"""
    rng = random.Random(0)
    for alphabet in ("ab", "abc", "abcd", string.ascii_lowercase[:8]):
        for _ in range(200):
            s = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 20)))
            assert length_of(solution, s) == brute_force(s), (s,)
