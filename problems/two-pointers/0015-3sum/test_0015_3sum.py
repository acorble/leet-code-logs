"""15. 3Sum のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
足して 0 になる 3 つ組を、**重複なく**すべて返す。組の順番も、組の中の順番も問わないので、並べ替えてから比べる。
"""

import itertools
import random


def three_sum(solution, nums):
    result = solution.Solution().threeSum(list(nums))
    return sorted(sorted(t) for t in result)


def brute_force(nums):
    return sorted({tuple(sorted(c)) for c in itertools.combinations(nums, 3) if sum(c) == 0})


def test_example_1(solution):
    assert three_sum(solution, [-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


def test_example_2(solution):
    assert three_sum(solution, [0, 1, 1]) == []


def test_example_3(solution):
    assert three_sum(solution, [0, 0, 0]) == [[0, 0, 0]]


def test_many_zeros(solution):
    # 同じ組を 2 回以上返さない
    assert three_sum(solution, [0, 0, 0, 0, 0]) == [[0, 0, 0]]


def test_duplicates_on_one_side_only(solution):
    assert three_sum(solution, [-2, 0, 0, 2, 2]) == [[-2, 0, 2]]


def test_random_against_brute_force(solution):
    rng = random.Random(15)
    for _ in range(500):
        nums = [rng.randint(-6, 6) for _ in range(rng.randint(3, 12))]
        assert three_sum(solution, nums) == [list(t) for t in brute_force(nums)], nums
