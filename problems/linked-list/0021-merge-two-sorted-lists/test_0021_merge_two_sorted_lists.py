"""21. Merge Two Sorted Lists のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
"""


def build_list(node_cls, values):
    """[1, 2, 4] のような配列から連結リストを作る。"""
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


def merge(solution, a, b):
    cls = solution.ListNode
    merged = solution.Solution().mergeTwoLists(build_list(cls, a), build_list(cls, b))
    return to_list(merged)


def test_example_1(solution):
    assert merge(solution, [1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]


def test_example_2(solution):
    assert merge(solution, [], []) == []


def test_example_3(solution):
    assert merge(solution, [], [0]) == [0]


def test_one_empty(solution):
    assert merge(solution, [1, 2, 3], []) == [1, 2, 3]


def test_no_overlap(solution):
    """片方が全部小さい。途中で一方が尽きる経路を通る。"""
    assert merge(solution, [1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge(solution, [4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]


def test_all_equal(solution):
    assert merge(solution, [2, 2], [2, 2]) == [2, 2, 2, 2]


def test_different_lengths(solution):
    assert merge(solution, [1], [2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge(solution, [5], [1, 2, 3, 4]) == [1, 2, 3, 4, 5]


def test_negative_values(solution):
    assert merge(solution, [-10, -3, 0], [-7, 5]) == [-10, -7, -3, 0, 5]
