"""242. Valid Anagram のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
これまでの解答は Java（attempts/*.java）なので、Python の解答が入るまではスキップする。
"""

import pytest


def is_anagram(solution, s, t):
    try:
        return solution.Solution().isAnagram(s, t)
    except NotImplementedError:
        pytest.skip("Python の解答はまだない（これまでの解答は attempts/*.java）")


def test_example_1(solution):
    assert is_anagram(solution, "anagram", "nagaram") is True


def test_example_2(solution):
    assert is_anagram(solution, "rat", "car") is False


def test_different_length(solution):
    assert is_anagram(solution, "a", "ab") is False


def test_same_letters_different_counts(solution):
    # 使っている文字の種類は同じでも、個数が違えばアナグラムではない
    assert is_anagram(solution, "aacc", "ccac") is False
