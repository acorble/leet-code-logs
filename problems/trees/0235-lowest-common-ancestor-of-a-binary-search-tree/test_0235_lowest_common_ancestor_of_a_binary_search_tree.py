"""235. Lowest Common Ancestor of a Binary Search Tree のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
入力は LeetCode と同じ「レベル順 + None」の配列表記で書く。
"""


def build_tree(node_cls, values):
    """[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5] のような配列から二分木を組み立てる。"""
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


def find(node, val):
    """値からノードを探す（BST の性質は使わず全探索）。"""
    if not node:
        return None
    if node.val == val:
        return node
    return find(node.left, val) or find(node.right, val)


def lca(solution, values, p_val, q_val):
    root = build_tree(solution.TreeNode, values)
    found = solution.Solution().lowestCommonAncestor(
        root, find(root, p_val), find(root, q_val)
    )
    return found.val if found else None


TREE = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]


def test_example_1(solution):
    """p と q が root の左右に分かれる → LCA は root。"""
    assert lca(solution, TREE, 2, 8) == 6


def test_example_2(solution):
    """q が p の子孫 → LCA は p 自身。"""
    assert lca(solution, TREE, 2, 4) == 2


def test_example_3(solution):
    assert lca(solution, [2, 1], 2, 1) == 2


def test_deep_pair(solution):
    """3 と 5 はどちらも 4 の子。"""
    assert lca(solution, TREE, 3, 5) == 4


def test_same_node(solution):
    """p と q が同じノードのとき、LCA はそのノード。"""
    assert lca(solution, TREE, 7, 7) == 7
