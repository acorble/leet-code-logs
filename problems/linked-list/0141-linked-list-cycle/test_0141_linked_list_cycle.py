"""141. Linked List Cycle のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
LeetCode と同じく、値の配列と `pos`（末尾が繋がる位置。-1 なら循環なし）で作る。
"""


def build_list(node_cls, values, pos=-1):
    """[3, 2, 0, -4] と pos=1 から、末尾が index 1 に繋がるリストを作る。"""
    if not values:
        return None

    nodes = [node_cls(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def has_cycle(solution, values, pos=-1):
    return solution.Solution().hasCycle(build_list(solution.ListNode, values, pos))


def test_example_1(solution):
    assert has_cycle(solution, [3, 2, 0, -4], 1) is True


def test_example_2(solution):
    assert has_cycle(solution, [1, 2], 0) is True


def test_example_3(solution):
    assert has_cycle(solution, [1], -1) is False


def test_empty(solution):
    assert has_cycle(solution, [], -1) is False


def test_no_cycle_long(solution):
    assert has_cycle(solution, [1, 2, 3, 4, 5], -1) is False


def test_self_loop(solution):
    """1 つのノードが自分自身を指すケース。"""
    assert has_cycle(solution, [1], 0) is True


def test_cycle_at_head(solution):
    """末尾が先頭に戻る（リスト全体が輪になっている）。"""
    assert has_cycle(solution, [1, 2, 3, 4], 0) is True


def test_cycle_at_tail(solution):
    """末尾が自分自身を指す。"""
    assert has_cycle(solution, [1, 2, 3], 2) is True


def test_duplicate_values_no_cycle(solution):
    """同じ値のノードが並んでいても、循環と誤判定しない。"""
    assert has_cycle(solution, [1, 1, 1, 1], -1) is False
