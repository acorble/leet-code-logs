"""1. Two Sum のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
LeetCode はインデックスの順序を問わないので、ここでも sorted() で比較する。
"""


def two_sum(solution, nums, target):
    return sorted(solution.Solution().twoSum(nums, target))


def test_example_1(solution):
    assert two_sum(solution, [2, 7, 11, 15], 9) == [0, 1]


def test_example_2(solution):
    assert two_sum(solution, [3, 2, 4], 6) == [1, 2]


def test_example_3(solution):
    assert two_sum(solution, [3, 3], 6) == [0, 1]
