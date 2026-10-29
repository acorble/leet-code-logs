"""19. Remove Nth Node From End of List のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
"""


def build_list(node_cls, values):
    """[1, 2, 3] のような配列から連結リストを作る。"""
    head = None
    for val in reversed(values):
        head = node_cls(val, head)
    return head


def to_list(head, limit=1000):
    out = []
    while head and len(out) < limit:
        out.append(head.val)
        head = head.next
    return out


def remove(solution, values, n):
    head = build_list(solution.ListNode, values)
    return to_list(solution.Solution().removeNthFromEnd(head, n))


def test_example_1(solution):
    assert remove(solution, [1, 2, 3, 4, 5], 2) == [1, 2, 3, 5]


def test_example_2(solution):
    assert remove(solution, [1], 1) == []


def test_example_3(solution):
    assert remove(solution, [1, 2], 1) == [1]


def test_remove_head(solution):
    """n がリストの長さに等しい = 先頭を消す。"""
    assert remove(solution, [1, 2], 2) == [2]
    assert remove(solution, [1, 2, 3, 4, 5], 5) == [2, 3, 4, 5]


def test_remove_tail(solution):
    assert remove(solution, [1, 2, 3, 4, 5], 1) == [1, 2, 3, 4]
