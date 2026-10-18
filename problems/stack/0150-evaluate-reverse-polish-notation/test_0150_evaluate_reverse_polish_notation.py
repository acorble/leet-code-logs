"""150. Evaluate Reverse Polish Notation のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
割り算は 0 方向への切り捨て（-7 / 2 は -3。Python の // とは違う）。
"""


def test_example_1(solution):
    # (2 + 1) * 3
    assert solution.Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9


def test_example_2(solution):
    # 4 + (13 / 5)
    assert solution.Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6


def test_example_3(solution):
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert solution.Solution().evalRPN(tokens) == 22


def test_single_number(solution):
    assert solution.Solution().evalRPN(["42"]) == 42


def test_subtraction_order(solution):
    # 先に積んだほうから引く: 3 - 5
    assert solution.Solution().evalRPN(["3", "5", "-"]) == -2


def test_negative_division_truncates_toward_zero(solution):
    assert solution.Solution().evalRPN(["-7", "2", "/"]) == -3
    assert solution.Solution().evalRPN(["7", "-2", "/"]) == -3
