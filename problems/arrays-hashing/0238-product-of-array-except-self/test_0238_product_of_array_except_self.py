"""238. Product of Array Except Self のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
answer[i] は nums[i] 以外の全要素の積。割り算を使わずに O(n) で求める。
これまでの解答は Java（attempts/*.java）なので、Python の解答が入るまではスキップする。
"""

import pytest


def product(solution, nums):
    try:
        return solution.Solution().productExceptSelf(nums)
    except NotImplementedError:
        pytest.skip("Python の解答はまだない（これまでの解答は attempts/*.java）")


def test_example_1(solution):
    assert product(solution, [1, 2, 3, 4]) == [24, 12, 8, 6]


def test_example_2(solution):
    assert product(solution, [-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_two_elements(solution):
    # 長さの最小は 2。それぞれ相手の値になる
    assert product(solution, [2, 3]) == [3, 2]


def test_two_zeros(solution):
    # 0 が 2 つあれば、どの位置も 0 を含む積になる
    assert product(solution, [0, 0, 5]) == [0, 0, 0]
