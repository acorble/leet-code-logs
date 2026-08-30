"""{number}. {title} のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
"""


def test_example_1(solution):
    assert solution.Solution().solve() is None
