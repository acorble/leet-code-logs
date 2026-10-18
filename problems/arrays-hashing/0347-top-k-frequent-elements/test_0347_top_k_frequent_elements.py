"""347. Top K Frequent Elements のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
答えの順番は問わないので、並べ替えてから比べる（答えは 1 通りに決まることが保証されている）。
これまでの解答は Java（attempts/*.java）なので、Python の解答が入るまではスキップする。
"""

import pytest


def top_k(solution, nums, k):
    try:
        result = solution.Solution().topKFrequent(nums, k)
    except NotImplementedError:
        pytest.skip("Python の解答はまだない（これまでの解答は attempts/*.java）")
    return sorted(result)


def test_example_1(solution):
    assert top_k(solution, [1, 1, 1, 2, 2, 3], 2) == [1, 2]


def test_example_2(solution):
    assert top_k(solution, [1], 1) == [1]


def test_example_3(solution):
    assert top_k(solution, [1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2) == [1, 2]


def test_negative_numbers(solution):
    assert top_k(solution, [-1, -1, 4, 4, 4, 7], 2) == [-1, 4]


def test_k_equals_distinct_count(solution):
    # k が値の種類数と同じなら、全種類を返す
    assert top_k(solution, [5, 5, 6], 2) == [5, 6]
