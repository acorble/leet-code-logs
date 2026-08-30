"""104. Maximum Depth of Binary Tree のテスト。

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


def max_depth(solution, values):
    return solution.Solution().maxDepth(build_tree(solution.TreeNode, values))


def test_example_1(solution):
    assert max_depth(solution, [3, 9, 20, None, None, 15, 7]) == 3


def test_example_2(solution):
    assert max_depth(solution, [1, None, 2]) == 2


def test_empty(solution):
    assert max_depth(solution, []) == 0


def test_single_node(solution):
    assert max_depth(solution, [1]) == 1


def test_skewed(solution):
    """左に一直線。深さはノード数と等しくなる。"""
    assert max_depth(solution, [1, 2, None, 3, None, 4]) == 4


def test_deeper_side_wins(solution):
    """左右で深さが違うとき、深いほうが答え。"""
    assert max_depth(solution, [1, 2, 3, 4, None, None, None, 5]) == 4
