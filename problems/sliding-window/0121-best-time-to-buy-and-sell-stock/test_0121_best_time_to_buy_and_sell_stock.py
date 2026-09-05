"""121. Best Time to Buy and Sell Stock のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
買った日より後に売る必要がある。利益が出せなければ 0。
"""

import random


def max_profit(solution, prices):
    return solution.Solution().maxProfit(prices)


def brute_force(prices):
    """全ペアを試す（正解の基準）。"""
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best


def test_example_1(solution):
    """1 で買って 6 で売る。"""
    assert max_profit(solution, [7, 1, 5, 3, 6, 4]) == 5


def test_example_2(solution):
    """下がり続けるので利益なし。"""
    assert max_profit(solution, [7, 6, 4, 3, 1]) == 0


def test_single_day(solution):
    """1 日しかないと売買できない。"""
    assert max_profit(solution, [5]) == 0


def test_increasing(solution):
    assert max_profit(solution, [1, 2, 3, 4, 5]) == 4


def test_all_equal(solution):
    assert max_profit(solution, [3, 3, 3]) == 0


def test_min_after_max(solution):
    """最安値が最高値より後にあるケース。買う前には売れない。"""
    assert max_profit(solution, [9, 10, 1, 2]) == 1


def test_dip_then_rise(solution):
    """途中でさらに安い日が来る。買う日を乗り換える必要がある。"""
    assert max_profit(solution, [5, 4, 1, 100]) == 99


def test_random_against_brute_force(solution):
    rng = random.Random(0)
    for _ in range(500):
        prices = [rng.randint(0, 50) for _ in range(rng.randint(1, 12))]
        assert max_profit(solution, prices) == brute_force(prices), (prices,)
