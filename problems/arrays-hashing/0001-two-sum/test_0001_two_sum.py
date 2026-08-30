"""1. Two Sum のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
"""


def test_example_1(solution):
    assert solution.Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_example_2(solution):
    assert solution.Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test_example_3(solution):
    assert solution.Solution().twoSum([3, 3], 6) == [0, 1]
