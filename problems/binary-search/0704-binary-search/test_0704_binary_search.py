"""704. Binary Search のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
制約上 nums は 1 要素以上・重複なし・昇順なので、空配列は試さない。
"""

import random


def search(solution, nums, target):
    return solution.Solution().search(nums, target)


def test_example_1(solution):
    assert search(solution, [-1, 0, 3, 5, 9, 12], 9) == 4


def test_example_2(solution):
    assert search(solution, [-1, 0, 3, 5, 9, 12], 2) == -1


def test_single_hit(solution):
    assert search(solution, [5], 5) == 0


def test_single_miss(solution):
    assert search(solution, [5], -5) == -1


def test_two_elements(solution):
    assert search(solution, [1, 2], 1) == 0
    assert search(solution, [1, 2], 2) == 1
    assert search(solution, [1, 2], 3) == -1


def test_first_and_last(solution):
    """両端は境界の扱いを間違えやすい。"""
    nums = [1, 3, 5, 7, 9, 11, 13]
    assert search(solution, nums, 1) == 0
    assert search(solution, nums, 13) == 6


def test_out_of_range(solution):
    nums = [1, 3, 5, 7, 9]
    assert search(solution, nums, 0) == -1
    assert search(solution, nums, 10) == -1


def test_exhaustive(solution):
    """長さ 1〜40 の全配列で、全要素と外れ値をすべて試す。"""
    for n in range(1, 41):
        nums = [i * 2 for i in range(n)]          # 0, 2, 4, ... 重複なしの昇順
        for i, value in enumerate(nums):
            assert search(solution, nums, value) == i, (nums, value)
        for miss in [-1, 1, nums[-1] + 1]:        # 手前・間・後ろの外れ値
            assert search(solution, nums, miss) == -1, (nums, miss)


def test_random(solution):
    """ランダムな昇順配列でも正しいか。"""
    rng = random.Random(0)
    for _ in range(200):
        nums = sorted(rng.sample(range(-100, 100), rng.randint(1, 30)))
        target = rng.randint(-105, 105)
        expected = nums.index(target) if target in nums else -1
        assert search(solution, nums, target) == expected, (nums, target)
