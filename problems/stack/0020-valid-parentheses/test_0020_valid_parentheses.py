"""20. Valid Parentheses のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
閉じ括弧は「いちばん最後に開いた括弧」と対応していなければならない。
"""


def test_example_1(solution):
    assert solution.Solution().isValid("()") is True


def test_example_2(solution):
    assert solution.Solution().isValid("()[]{}") is True


def test_example_3(solution):
    assert solution.Solution().isValid("(]") is False


def test_example_4(solution):
    assert solution.Solution().isValid("([])") is True


def test_example_5(solution):
    # 種類の数は合っているが、閉じる順番が違う
    assert solution.Solution().isValid("([)]") is False


def test_close_without_open(solution):
    # Stack が空のときに閉じ括弧が来る
    assert solution.Solution().isValid("]") is False


def test_unclosed_left_over(solution):
    # 最後まで読んでも開き括弧が残っている
    assert solution.Solution().isValid("((") is False
