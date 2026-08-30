"""102. Binary Tree Level Order Traversal のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
入力は LeetCode と同じ「レベル順 + null」の配列表記で書き、build_tree で木にする。
"""


def build_tree(node_cls, values):
    """[3, 9, 20, None, None, 15, 7] のような配列から二分木を組み立てる。"""
    if not values or values[0] is None:
        return None

    root = node_cls(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = node_cls(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = node_cls(values[i])
                queue.append(node.right)
            i += 1
    return root


def level_order(solution, values):
    root = build_tree(solution.TreeNode, values)
    return solution.Solution().levelOrder(root)


def test_example_1(solution):
    assert level_order(solution, [3, 9, 20, None, None, 15, 7]) == [[3], [9, 20], [15, 7]]


def test_example_2(solution):
    assert level_order(solution, [1]) == [[1]]


def test_example_3(solution):
    assert level_order(solution, []) == []


def test_left_skewed(solution):
    """左に一直線。各レベルにノードが 1 つずつ。"""
    assert level_order(solution, [1, 2, None, 3]) == [[1], [2], [3]]


def test_right_skewed(solution):
    assert level_order(solution, [1, None, 2, None, 3]) == [[1], [2], [3]]
