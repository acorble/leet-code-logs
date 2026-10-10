"""145. Binary Tree Postorder Traversal のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
後順 (postorder) は 左 → 右 → 自分 の順。
"""


def build_tree(node_cls, values):
    """[1, None, 2, 3] のような配列から二分木を組み立てる。"""
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


def postorder(solution, values):
    root = build_tree(solution.TreeNode, values)
    return solution.Solution().postorderTraversal(root)


def test_example_1(solution):
    assert postorder(solution, [1, None, 2, 3]) == [3, 2, 1]


def test_example_2(solution):
    values = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
    assert postorder(solution, values) == [4, 6, 7, 5, 2, 9, 8, 3, 1]


def test_example_3_empty(solution):
    assert postorder(solution, []) == []


def test_example_4_single(solution):
    assert postorder(solution, [1]) == [1]


def test_left_skewed(solution):
    # 1 -> 2 -> 3 と左にだけ伸びる木。葉から順に出てくる
    assert postorder(solution, [1, 2, None, 3]) == [3, 2, 1]
