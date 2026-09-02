"""199. Binary Tree Right Side View のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
入力は LeetCode と同じ「レベル順 + None」の配列表記で書く。
"""


def build_tree(node_cls, values):
    """[1, 2, 3, None, 5, None, 4] のような配列から二分木を組み立てる。"""
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


def right_side(solution, values):
    return solution.Solution().rightSideView(build_tree(solution.TreeNode, values))


def test_example_1(solution):
    assert right_side(solution, [1, 2, 3, None, 5, None, 4]) == [1, 3, 4]


def test_example_2(solution):
    assert right_side(solution, [1, None, 3]) == [1, 3]


def test_example_3(solution):
    assert right_side(solution, []) == []


def test_single_node(solution):
    assert right_side(solution, [1]) == [1]


def test_left_skewed(solution):
    """右に何も無くても、各層の唯一のノードが見える。"""
    assert right_side(solution, [1, 2, None, 3]) == [1, 2, 3]


def test_left_subtree_is_deeper(solution):
    """右の部分木より左の部分木が深いとき、下の層では左のノードが見える。"""
    assert right_side(solution, [1, 2, 3, 4]) == [1, 3, 4]
