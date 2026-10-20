"""853. Car Fleet のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
"""


def test_example_1(solution):
    assert solution.Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3


def test_example_2(solution):
    assert solution.Solution().carFleet(10, [3], [3]) == 1


def test_example_3(solution):
    assert solution.Solution().carFleet(100, [0, 2, 4], [4, 2, 1]) == 1


def test_no_catch_up_within_same_integer_second(solution):
    # 前の車 1.2 秒、後ろの車 1.5 秒で追いつけない。切り上げると両方 2 秒になる
    assert solution.Solution().carFleet(10, [4, 1], [5, 6]) == 2


def test_catch_up_exactly_at_target(solution):
    # 両方ちょうど 1 秒でゴールに着く → 同じ集団
    assert solution.Solution().carFleet(10, [5, 0], [5, 10]) == 1
