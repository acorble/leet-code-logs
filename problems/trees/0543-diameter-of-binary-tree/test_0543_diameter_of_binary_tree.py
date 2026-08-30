"""543. Diameter of Binary Tree のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
入力は LeetCode と同じ「レベル順 + None」の配列表記で書く。
制約上ノードは 1 個以上あるので、空の木は試さない。
"""


def build_tree(node_cls, values):
    """[1, 2, 3, 4, 5] のような配列から二分木を組み立てる。"""
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


def diameter(solution, values):
    return solution.Solution().diameterOfBinaryTree(build_tree(solution.TreeNode, values))


def test_example_1(solution):
    """4-2-1-3 または 5-2-1-3 が最長で、辺の数は 3。"""
    assert diameter(solution, [1, 2, 3, 4, 5]) == 3


def test_example_2(solution):
    assert diameter(solution, [1, 2]) == 1


def test_single_node(solution):
    assert diameter(solution, [1]) == 0


def test_skewed(solution):
    """左に一直線。直径は根を通る 1 本道。"""
    assert diameter(solution, [1, 2, None, 3, None, 4]) == 3


def test_not_through_root(solution):
    """最長経路が根を通らないケース。

    8-6-4-2-5-7-9 の 6 辺が最長で、これは根 (1) を通らない。
    根を通る最長は 8-6-4-2-1 の 4 辺しかない。
    """
    values = [1, 2, None, 4, 5, 6, None, None, 7, 8, None, None, 9]
    assert diameter(solution, values) == 6
