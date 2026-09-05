"""875. Koko Eating Bananas のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
制約上 len(piles) <= h なので、必ず答えが存在する。
"""

import math
import random


def min_speed(solution, piles, h):
    return solution.Solution().minEatingSpeed(piles, h)


def brute_force(piles, h):
    """1 から順に試して、最初に間に合う速度を返す（正解の基準）。"""
    for k in range(1, max(piles) + 1):
        if sum(math.ceil(pile / k) for pile in piles) <= h:
            return k
    return max(piles)


def test_example_1(solution):
    assert min_speed(solution, [3, 6, 7, 11], 8) == 4


def test_example_2(solution):
    """h が山の数と同じ → 一番大きい山を 1 時間で食べ切る速度が要る。"""
    assert min_speed(solution, [30, 11, 23, 4, 20], 5) == 30


def test_example_3(solution):
    assert min_speed(solution, [30, 11, 23, 4, 20], 6) == 23


def test_single_pile(solution):
    assert min_speed(solution, [312884470], 968709470) == 1
    assert min_speed(solution, [10], 1) == 10
    assert min_speed(solution, [10], 2) == 5


def test_answer_is_one(solution):
    """時間が十分あるとき、最小速度は 1。"""
    assert min_speed(solution, [1, 1, 1, 1], 100) == 1


def test_answer_is_max(solution):
    """h == 山の数のとき、答えは必ず最大の山。"""
    assert min_speed(solution, [5, 8, 6], 3) == 8


def test_exhaustive(solution):
    """小さい入力を総当たりで、素朴な実装と突き合わせる。"""
    rng = random.Random(0)
    for _ in range(300):
        piles = [rng.randint(1, 20) for _ in range(rng.randint(1, 6))]
        h = rng.randint(len(piles), len(piles) + 25)
        assert min_speed(solution, piles, h) == brute_force(piles, h), (piles, h)


def test_large_values(solution):
    """値が大きくてもループではなく二分探索で解けているか。"""
    piles = [1000000000, 1000000000, 1000000000]
    assert min_speed(solution, piles, 3) == 1000000000
    assert min_speed(solution, piles, 6) == 500000000
