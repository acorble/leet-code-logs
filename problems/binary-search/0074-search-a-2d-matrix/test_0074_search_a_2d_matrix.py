"""74. Search a 2D Matrix のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
制約上、行も列も 1 以上（空の matrix は来ない）。
"""

import random

MATRIX = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]


def search(solution, matrix, target):
    return solution.Solution().searchMatrix(matrix, target)


def test_example_1(solution):
    assert search(solution, MATRIX, 3) is True


def test_example_2(solution):
    assert search(solution, MATRIX, 13) is False


def test_corners(solution):
    """四隅は境界の扱いを間違えやすい。"""
    assert search(solution, MATRIX, 1) is True
    assert search(solution, MATRIX, 60) is True


def test_row_boundaries(solution):
    """行をまたぐ位置（行末と次の行頭）。"""
    assert search(solution, MATRIX, 7) is True
    assert search(solution, MATRIX, 10) is True


def test_out_of_range(solution):
    assert search(solution, MATRIX, 0) is False
    assert search(solution, MATRIX, 61) is False


def test_single_cell(solution):
    assert search(solution, [[1]], 1) is True
    assert search(solution, [[1]], 2) is False


def test_single_row(solution):
    assert search(solution, [[1, 3, 5]], 5) is True
    assert search(solution, [[1, 3, 5]], 4) is False


def test_single_column(solution):
    assert search(solution, [[1], [3], [5]], 3) is True
    assert search(solution, [[1], [3], [5]], 4) is False


def test_exhaustive(solution):
    """いろいろな形の行列で、全要素と外れ値をすべて試す。"""
    for rows in range(1, 8):
        for cols in range(1, 8):
            values = [i * 2 for i in range(rows * cols)]
            matrix = [values[r * cols:(r + 1) * cols] for r in range(rows)]
            for value in values:
                assert search(solution, matrix, value) is True, (matrix, value)
            for miss in [-1, 1, values[-1] + 1]:
                assert search(solution, matrix, miss) is False, (matrix, miss)


def test_random(solution):
    rng = random.Random(0)
    for _ in range(200):
        rows, cols = rng.randint(1, 6), rng.randint(1, 6)
        values = sorted(rng.sample(range(-100, 100), rows * cols))
        matrix = [values[r * cols:(r + 1) * cols] for r in range(rows)]
        target = rng.randint(-105, 105)
        assert search(solution, matrix, target) is (target in values), (matrix, target)
