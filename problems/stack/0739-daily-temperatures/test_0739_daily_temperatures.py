"""739. Daily Temperatures のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
各日について「より暖かい日が来るまで何日待つか」。来なければ 0。
"""


def test_example_1(solution):
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    assert solution.Solution().dailyTemperatures(temps) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_example_2(solution):
    assert solution.Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]


def test_example_3(solution):
    assert solution.Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0]


def test_single_day(solution):
    assert solution.Solution().dailyTemperatures([50]) == [0]


def test_equal_is_not_warmer(solution):
    # 同じ温度は「より暖かい」に含まない
    assert solution.Solution().dailyTemperatures([70, 70, 70]) == [0, 0, 0]


def test_decreasing(solution):
    assert solution.Solution().dailyTemperatures([90, 80, 70, 60]) == [0, 0, 0, 0]
