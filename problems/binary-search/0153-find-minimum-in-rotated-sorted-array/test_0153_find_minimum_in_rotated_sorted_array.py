"""153. Find Minimum in Rotated Sorted Array のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
制約上、値は重複なし・要素は 1 個以上。
"""

import random


def find_min(solution, nums):
    return solution.Solution().findMin(nums)


def test_example_1(solution):
    assert find_min(solution, [3, 4, 5, 1, 2]) == 1


def test_example_2(solution):
    assert find_min(solution, [4, 5, 6, 7, 0, 1, 2]) == 0


def test_example_3(solution):
    """回転していない（0 回転）ケース。"""
    assert find_min(solution, [11, 13, 15, 17]) == 11


def test_single(solution):
    assert find_min(solution, [1]) == 1


def test_two(solution):
    assert find_min(solution, [1, 2]) == 1
    assert find_min(solution, [2, 1]) == 1


def test_rotated_by_one(solution):
    """最小値が末尾にあるケース。"""
    assert find_min(solution, [2, 3, 4, 5, 1]) == 1


def test_rotated_almost_full(solution):
    """最小値が 2 番目にあるケース。"""
    assert find_min(solution, [5, 1, 2, 3, 4]) == 1


def test_exhaustive_rotations(solution):
    """長さ 1〜12 の配列を、あり得るすべての回転量で試す。"""
    for n in range(1, 13):
        base = [i * 3 for i in range(n)]
        for k in range(n):
            rotated = base[k:] + base[:k]
            assert find_min(solution, rotated) == base[0], (rotated,)


def test_random(solution):
    rng = random.Random(0)
    for _ in range(300):
        n = rng.randint(1, 30)
        base = sorted(rng.sample(range(-1000, 1000), n))
        k = rng.randrange(n)
        rotated = base[k:] + base[:k]
        assert find_min(solution, rotated) == base[0], (rotated,)
