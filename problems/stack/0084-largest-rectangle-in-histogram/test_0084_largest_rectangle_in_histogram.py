"""84. Largest Rectangle in Histogram のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
"""


def test_example_1(solution):
    assert solution.Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10


def test_example_2(solution):
    assert solution.Solution().largestRectangleArea([2, 4]) == 4


def test_single_bar(solution):
    assert solution.Solution().largestRectangleArea([5]) == 5


def test_increasing(solution):
    # 最後まで pop されず、ループ後の処理で面積が決まる: 3 * 3 = 9
    assert solution.Solution().largestRectangleArea([1, 2, 3, 4, 5]) == 9


def test_decreasing(solution):
    # pop した棒の左端を引き継がないと 3 * 3 = 9 を逃す
    assert solution.Solution().largestRectangleArea([5, 4, 3, 2, 1]) == 9


def test_equal_heights(solution):
    assert solution.Solution().largestRectangleArea([2, 2, 2]) == 6


def test_zero_height(solution):
    assert solution.Solution().largestRectangleArea([2, 0, 2]) == 2
