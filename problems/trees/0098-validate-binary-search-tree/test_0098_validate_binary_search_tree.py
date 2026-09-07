"""98. Validate Binary Search Tree のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
BST の条件は「左部分木の全ノード < 自分 < 右部分木の全ノード」。
直前の親だけでなく、部分木の全体と比べる必要がある。
"""

import itertools
import random


def build_tree(node_cls, values):
    """[2, 1, 3] のような配列から二分木を組み立てる。"""
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


def in_order(node, out):
    if not node:
        return
    in_order(node.left, out)
    out.append(node.val)
    in_order(node.right, out)


def brute_force(root):
    """中順走査が狭義単調増加なら BST（正解の基準）。"""
    out = []
    in_order(root, out)
    return all(a < b for a, b in zip(out, out[1:]))


def is_valid(solution, values):
    return solution.Solution().isValidBST(build_tree(solution.TreeNode, values))


def test_example_1(solution):
    assert is_valid(solution, [2, 1, 3]) is True


def test_example_2(solution):
    """4 は 5 の右部分木にあるが、5 より小さいので不正。"""
    assert is_valid(solution, [5, 1, 4, None, None, 3, 6]) is False


def test_single(solution):
    assert is_valid(solution, [1]) is True


def test_empty(solution):
    assert is_valid(solution, []) is True


def test_duplicate_is_invalid(solution):
    """等しい値は許されない（狭義）。"""
    assert is_valid(solution, [2, 2]) is False
    assert is_valid(solution, [2, 1, 2]) is False


def test_violation_deep_in_subtree(solution):
    """親とだけ比べると見逃すケース。

    3 は親 (6) より小さく左にあるので局所的には正しいが、
    祖先の 5 より小さいのに右部分木にいるので不正。
    """
    assert is_valid(solution, [5, 4, 6, None, None, 3, 7]) is False


def test_left_skewed_valid(solution):
    assert is_valid(solution, [3, 2, None, 1]) is True


def test_right_skewed_valid(solution):
    assert is_valid(solution, [1, None, 2, None, 3]) is True


def test_negative_values(solution):
    assert is_valid(solution, [0, -1, 1]) is True


def test_exhaustive_small_trees(solution):
    """小さい木の形と値の組み合わせを総当たりで、中順走査と突き合わせる。"""
    shapes = [
        [1],
        [1, 2],
        [1, None, 2],
        [1, 2, 3],
        [1, 2, None, 3],
        [1, None, 2, None, 3],
        [1, 2, 3, 4],
        [1, 2, 3, None, 4],
        [1, 2, 3, None, None, 4],
        [1, 2, 3, 4, 5, 6, 7],
    ]
    for shape in shapes:
        slots = sum(1 for v in shape if v is not None)
        for combo in itertools.product(range(1, 5), repeat=slots):
            it = iter(combo)
            values = [next(it) if v is not None else None for v in shape]
            tree = build_tree(solution.TreeNode, values)
            got = solution.Solution().isValidBST(tree)
            assert got == brute_force(build_tree(solution.TreeNode, values)), values


def test_random_trees(solution):
    rng = random.Random(0)
    for _ in range(500):
        n = rng.randint(1, 12)
        values = [rng.choice([rng.randint(1, 20), None]) for _ in range(n)]
        values[0] = rng.randint(1, 20)
        tree = build_tree(solution.TreeNode, values)
        expected = brute_force(build_tree(solution.TreeNode, values))
        assert solution.Solution().isValidBST(tree) == expected, values
