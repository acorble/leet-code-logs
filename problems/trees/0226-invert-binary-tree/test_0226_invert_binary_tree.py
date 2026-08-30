"""226. Invert Binary Tree のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
入出力とも LeetCode と同じ「レベル順 + None」の配列表記で書く。
"""


def build_tree(node_cls, values):
    """[4, 2, 7, 1, 3, 6, 9] のような配列から二分木を組み立てる。"""
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


def to_list(root):
    """木をレベル順の配列に戻す。末尾の None は落とす。"""
    if not root:
        return []
    out = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def invert(solution, values):
    root = build_tree(solution.TreeNode, values)
    return to_list(solution.Solution().invertTree(root))


def test_example_1(solution):
    assert invert(solution, [4, 2, 7, 1, 3, 6, 9]) == [4, 7, 2, 9, 6, 3, 1]


def test_example_2(solution):
    assert invert(solution, [2, 1, 3]) == [2, 3, 1]


def test_example_3(solution):
    assert invert(solution, []) == []


def test_single_node(solution):
    assert invert(solution, [1]) == [1]


def test_skewed(solution):
    """左に一直線の木は、右に一直線の木になる。"""
    assert invert(solution, [1, 2, None, 3]) == [1, None, 2, None, 3]


def test_twice_restores(solution):
    """2 回反転すると元に戻る。"""
    cls = solution.TreeNode
    s = solution.Solution()
    values = [4, 2, 7, 1, 3, 6, 9]
    root = build_tree(cls, values)
    assert to_list(s.invertTree(s.invertTree(root))) == values
