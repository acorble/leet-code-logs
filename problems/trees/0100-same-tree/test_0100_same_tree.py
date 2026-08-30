"""100. Same Tree のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
入力は LeetCode と同じ「レベル順 + None」の配列表記で書く。
"""


def build_tree(node_cls, values):
    """[1, 2, 3] のような配列から二分木を組み立てる。"""
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


def is_same(solution, p_values, q_values):
    cls = solution.TreeNode
    return solution.Solution().isSameTree(
        build_tree(cls, p_values), build_tree(cls, q_values)
    )


def test_example_1(solution):
    assert is_same(solution, [1, 2, 3], [1, 2, 3]) is True


def test_example_2(solution):
    """同じ値だが左右が入れ替わっている（形が違う）。"""
    assert is_same(solution, [1, 2], [1, None, 2]) is False


def test_example_3(solution):
    """形は同じだが値が違う。"""
    assert is_same(solution, [1, 2, 1], [1, 1, 2]) is False


def test_both_empty(solution):
    assert is_same(solution, [], []) is True


def test_one_empty(solution):
    assert is_same(solution, [1], []) is False


def test_prefix_shorter(solution):
    """p のほうが深い。途中まで同じでも False。"""
    assert is_same(solution, [1, 2, 3, 4], [1, 2, 3]) is False
