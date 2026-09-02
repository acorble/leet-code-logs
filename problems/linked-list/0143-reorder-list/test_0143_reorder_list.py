"""143. Reorder List のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
reorderList は返り値を持たず、リストをその場で書き換える。
"""


def build_list(node_cls, values):
    """[1, 2, 3, 4] のような配列から連結リストを作る。"""
    head = None
    for val in reversed(values):
        head = node_cls(val, head)
    return head


def to_list(head, limit=1000):
    """連結リストを配列に戻す。循環していたら limit で打ち切って気づけるようにする。"""
    out = []
    while head and len(out) < limit:
        out.append(head.val)
        head = head.next
    return out


def reorder(solution, values):
    head = build_list(solution.ListNode, values)
    assert solution.Solution().reorderList(head) is None
    return to_list(head)


def test_example_1(solution):
    assert reorder(solution, [1, 2, 3, 4]) == [1, 4, 2, 3]


def test_example_2(solution):
    assert reorder(solution, [1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]


def test_single(solution):
    assert reorder(solution, [1]) == [1]


def test_two(solution):
    assert reorder(solution, [1, 2]) == [1, 2]


def test_three(solution):
    assert reorder(solution, [1, 2, 3]) == [1, 3, 2]


def test_six(solution):
    assert reorder(solution, [1, 2, 3, 4, 5, 6]) == [1, 6, 2, 5, 3, 4]


def test_seven(solution):
    assert reorder(solution, [1, 2, 3, 4, 5, 6, 7]) == [1, 7, 2, 6, 3, 5, 4]


def test_no_cycle(solution):
    """末尾が None で終わっているか（循環していないか）。"""
    head = build_list(solution.ListNode, [1, 2, 3, 4, 5])
    solution.Solution().reorderList(head)
    assert len(to_list(head)) == 5
