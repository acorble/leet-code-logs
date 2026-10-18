"""36. Valid Sudoku のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
埋まっているマスだけを見て、行・列・3x3 のブロックに同じ数字が重複していないかを判定する（解けるかどうかは問わない）。
これまでの解答は Java（attempts/*.java）なので、Python の解答が入るまではスキップする。
"""

import pytest

EXAMPLE_1 = [
    "53..7....",
    "6..195...",
    ".98....6.",
    "8...6...3",
    "4..8.3..1",
    "7...2...6",
    ".6....28.",
    "...419..5",
    "....8..79",
]

EMPTY = ["." * 9] * 9


def board_of(rows):
    return [list(row) for row in rows]


def is_valid(solution, rows):
    try:
        return solution.Solution().isValidSudoku(board_of(rows))
    except NotImplementedError:
        pytest.skip("Python の解答はまだない（これまでの解答は attempts/*.java）")


def with_cells(rows, cells):
    """空の盤面などに、{(行, 列): 数字} のマスを書き込んだ盤面を作る。"""
    grid = [list(row) for row in rows]
    for (r, c), v in cells.items():
        grid[r][c] = v
    return ["".join(row) for row in grid]


def test_example_1(solution):
    assert is_valid(solution, EXAMPLE_1) is True


def test_example_2(solution):
    # 左上を 8 にすると、左の列と左上のブロックに 8 が 2 つになる
    rows = with_cells(EXAMPLE_1, {(0, 0): "8"})
    assert is_valid(solution, rows) is False


def test_empty_board(solution):
    assert is_valid(solution, EMPTY) is True


def test_duplicate_in_row(solution):
    assert is_valid(solution, with_cells(EMPTY, {(4, 0): "7", (4, 8): "7"})) is False


def test_duplicate_in_column(solution):
    assert is_valid(solution, with_cells(EMPTY, {(0, 5): "3", (8, 5): "3"})) is False


def test_duplicate_only_in_box(solution):
    # 行も列も違うが、同じ 3x3 ブロックの中で重複している
    assert is_valid(solution, with_cells(EMPTY, {(6, 6): "9", (8, 8): "9"})) is False
