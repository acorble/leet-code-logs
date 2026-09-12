"""230. Kth Smallest Element in a BST のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
制約上 1 <= k <= ノード数 で、値に重複は無い。
"""

import random


def build_tree(node_cls, values):
    """[3, 1, 4, None, 2] のような配列から二分木を組み立てる。"""
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


def insert_bst(node_cls, root, val):
    """BST の規則に従って値を挿入する（ランダムな BST を作るため）。"""
    if root is None:
        return node_cls(val)
    if val < root.val:
        root.left = insert_bst(node_cls, root.left, val)
    else:
        root.right = insert_bst(node_cls, root.right, val)
    return root


def kth(solution, values, k):
    return solution.Solution().kthSmallest(build_tree(solution.TreeNode, values), k)


def test_example_1(solution):
    assert kth(solution, [3, 1, 4, None, 2], 1) == 1


def test_example_2(solution):
    assert kth(solution, [5, 3, 6, 2, 4, None, None, 1], 3) == 3


def test_single(solution):
    assert kth(solution, [7], 1) == 7


def test_k_is_largest(solution):
    """k = ノード数なら最大値。"""
    assert kth(solution, [3, 1, 4, None, 2], 4) == 4


def test_every_k(solution):
    """同じ木で k を 1 から n まで全部試す。"""
    values = [5, 3, 6, 2, 4, None, None, 1]
    for k, expected in enumerate([1, 2, 3, 4, 5, 6], start=1):
        assert kth(solution, values, k) == expected


def test_skewed(solution):
    """右に一直線の BST。"""
    assert kth(solution, [1, None, 2, None, 3, None, 4], 3) == 3


def test_random_bst(solution):
    """ランダムに BST を作り、ソート済み配列と突き合わせる。"""
    rng = random.Random(0)
    for _ in range(300):
        vals = rng.sample(range(-50, 50), rng.randint(1, 15))
        root = None
        for v in vals:
            root = insert_bst(solution.TreeNode, root, v)
        expected = sorted(vals)
        for k in range(1, len(vals) + 1):
            assert solution.Solution().kthSmallest(root, k) == expected[k - 1], (vals, k)
