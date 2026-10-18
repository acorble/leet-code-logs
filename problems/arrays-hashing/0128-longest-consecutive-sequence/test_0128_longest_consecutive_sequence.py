"""128. Longest Consecutive Sequence のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
配列の中で、連続した整数（1, 2, 3, … のように 1 ずつ増える並び）が最長で何個あるか。並び順は問わない。O(n) で解くこと。
これまでの解答は Java（attempts/*.java）なので、Python の解答が入るまではスキップする。
"""

import pytest


def longest(solution, nums):
    try:
        return solution.Solution().longestConsecutive(nums)
    except NotImplementedError:
        pytest.skip("Python の解答はまだない（これまでの解答は attempts/*.java）")


def test_example_1(solution):
    assert longest(solution, [100, 4, 200, 1, 3, 2]) == 4


def test_example_2(solution):
    assert longest(solution, [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_example_3(solution):
    # 重複は 1 つとして数える
    assert longest(solution, [1, 0, 1, 2]) == 3


def test_empty(solution):
    assert longest(solution, []) == 0


def test_negative_numbers(solution):
    assert longest(solution, [-2, -1, 0, 5]) == 3


def test_many_isolated_values_is_fast(solution):
    # 値がすべて離れている（長さ 1 の並びが 10^5 本）。O(n²) だとここで時間がかかる
    nums = list(range(0, 200_000, 2))
    assert longest(solution, nums) == 1
