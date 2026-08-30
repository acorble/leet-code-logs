"""572. Subtree of Another Tree のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
入力は LeetCode と同じ「レベル順 + None」の配列表記で書く。
"""


def build_tree(node_cls, values):
    """[3, 4, 5, 1, 2] のような配列から二分木を組み立てる。"""
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


def is_subtree(solution, root_values, sub_values):
    cls = solution.TreeNode
    return solution.Solution().isSubtree(
        build_tree(cls, root_values), build_tree(cls, sub_values)
    )


def test_example_1(solution):
    assert is_subtree(solution, [3, 4, 5, 1, 2], [4, 1, 2]) is True


def test_example_2(solution):
    """4 の下に 0 がぶら下がっているので、部分木として一致しない。"""
    values = [3, 4, 5, 1, 2, None, None, None, None, 0]
    assert is_subtree(solution, values, [4, 1, 2]) is False


def test_whole_tree(solution):
    """木全体も自分自身の部分木とみなす。"""
    assert is_subtree(solution, [1, 2, 3], [1, 2, 3]) is True


def test_value_matches_but_shape_differs(solution):
    """根の値は一致するが形が違う。"""
    assert is_subtree(solution, [1, 1], [1, None, 1]) is False


def test_single_node(solution):
    assert is_subtree(solution, [3, 4, 5], [5]) is True
    assert is_subtree(solution, [3, 4, 5], [6]) is False
