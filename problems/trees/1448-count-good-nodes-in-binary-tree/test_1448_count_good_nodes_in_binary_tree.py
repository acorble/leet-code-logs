"""1448. Count Good Nodes in Binary Tree のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
入力は LeetCode と同じ「レベル順 + None」の配列表記で書く。
"""


def build_tree(node_cls, values):
    """[3, 1, 4, 3, None, 1, 5] のような配列から二分木を組み立てる。"""
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


def good_nodes(solution, values):
    return solution.Solution().goodNodes(build_tree(solution.TreeNode, values))


def test_example_1(solution):
    """good なのは 3(root), 3(左下), 4, 5 の 4 つ。"""
    assert good_nodes(solution, [3, 1, 4, 3, None, 1, 5]) == 4


def test_example_2(solution):
    """3(root), 3(左), 4 の 3 つ。2 は祖先の 3 より小さいので good ではない。"""
    assert good_nodes(solution, [3, 3, None, 4, 2]) == 3


def test_example_3(solution):
    """根だけの木。根は必ず good。"""
    assert good_nodes(solution, [1]) == 1


def test_all_increasing(solution):
    """右に一直線で増加。全ノードが good。"""
    assert good_nodes(solution, [1, None, 2, None, 3, None, 4]) == 4


def test_all_decreasing(solution):
    """右に一直線で減少。good は根だけ。"""
    assert good_nodes(solution, [4, None, 3, None, 2, None, 1]) == 1


def test_equal_values(solution):
    """祖先と同じ値でも good（「より大きいものが無い」が条件）。"""
    assert good_nodes(solution, [2, 2, 2]) == 3


def test_max_is_not_the_parent(solution):
    """直前の親ではなく、経路上の最大と比べる必要がある。

    5 -> 1 -> 4 の 4 は、親 (1) より大きいが祖先の 5 より小さいので good ではない。
    """
    assert good_nodes(solution, [5, 1, None, 4]) == 1


def test_siblings_are_independent(solution):
    """左右の枝は互いに影響しない（path を pop し忘れると壊れる）。"""
    assert good_nodes(solution, [2, 5, 3]) == 3
