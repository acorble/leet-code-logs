"""206. Reverse Linked List のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
"""


def build_list(node_cls, values):
    """[1, 2, 3] のような配列から連結リストを作る。"""
    head = None
    for val in reversed(values):
        head = node_cls(val, head)
    return head


def to_list(head, limit=1000):
    """連結リストを配列に戻す。循環していたら limit で打ち切る。"""
    out = []
    while head and len(out) < limit:
        out.append(head.val)
        head = head.next
    return out


def reverse(solution, values):
    head = build_list(solution.ListNode, values)
    return to_list(solution.Solution().reverseList(head))


def test_example_1(solution):
    assert reverse(solution, [1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


def test_example_2(solution):
    assert reverse(solution, [1, 2]) == [2, 1]


def test_example_3(solution):
    assert reverse(solution, []) == []


def test_single(solution):
    assert reverse(solution, [1]) == [1]


def test_duplicate_values(solution):
    assert reverse(solution, [1, 1, 2, 2]) == [2, 2, 1, 1]


def test_negative_values(solution):
    assert reverse(solution, [-1, 0, 3]) == [3, 0, -1]


def test_long(solution):
    values = list(range(50))
    assert reverse(solution, values) == list(reversed(values))
