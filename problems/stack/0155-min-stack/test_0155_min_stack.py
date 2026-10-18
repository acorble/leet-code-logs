"""155. Min Stack のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
push / pop / top / getMin のすべてを O(1) で行うスタック。
"""


def test_example_1(solution):
    s = solution.MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2


def test_min_restored_after_pop(solution):
    # 最小値を pop したら、その前の最小値に戻る
    s = solution.MinStack()
    s.push(5)
    s.push(3)
    s.push(7)
    s.push(1)
    assert s.getMin() == 1
    s.pop()
    assert s.getMin() == 3
    s.pop()
    s.pop()
    assert s.getMin() == 5


def test_duplicate_minimum(solution):
    # 同じ最小値が 2 回積まれても、1 回 pop しただけでは最小値は変わらない
    s = solution.MinStack()
    s.push(2)
    s.push(1)
    s.push(1)
    s.pop()
    assert s.getMin() == 1
    s.pop()
    assert s.getMin() == 2


def test_single_element(solution):
    s = solution.MinStack()
    s.push(42)
    assert s.top() == 42
    assert s.getMin() == 42
