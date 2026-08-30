"""217. Contains Duplicate のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
"""


def test_example_1(solution):
    assert solution.Solution().containsDuplicate([1, 2, 3, 1]) is True


def test_example_2(solution):
    assert solution.Solution().containsDuplicate([1, 2, 3, 4]) is False


def test_example_3(solution):
    assert solution.Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


def test_empty(solution):
    assert solution.Solution().containsDuplicate([]) is False


def test_single(solution):
    assert solution.Solution().containsDuplicate([1]) is False
