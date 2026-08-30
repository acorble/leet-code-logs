"""110. Balanced Binary Tree のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
入力は LeetCode と同じ「レベル順 + None」の配列表記で書く。
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


def is_balanced(solution, values):
    return solution.Solution().isBalanced(build_tree(solution.TreeNode, values))


def test_example_1(solution):
    assert is_balanced(solution, [3, 9, 20, None, None, 15, 7]) is True


def test_example_2(solution):
    assert is_balanced(solution, [1, 2, 2, 3, 3, None, None, 4, 4]) is False


def test_example_3(solution):
    assert is_balanced(solution, []) is True


def test_skewed(solution):
    """左に一直線。深さの差が 2 になる。"""
    assert is_balanced(solution, [1, 2, None, 3]) is False


def test_deep_but_balanced(solution):
    assert is_balanced(solution, [1, 2, 3, 4, None, None, 5]) is True


def test_unbalanced_deep_inside(solution):
    """根は釣り合っているが、深い位置の部分木が崩れている。"""
    values = [1, 2, 3, 4, 5, None, None, 6, None, None, None, 7]
    assert is_balanced(solution, values) is False


def test_called_twice(solution):
    """インスタンス変数を使っているので、続けて呼んでも結果が混ざらないか。"""
    s = solution.Solution()
    cls = solution.TreeNode
    assert s.isBalanced(build_tree(cls, [1, 2, None, 3])) is False
    assert s.isBalanced(build_tree(cls, [3, 9, 20, None, None, 15, 7])) is True
