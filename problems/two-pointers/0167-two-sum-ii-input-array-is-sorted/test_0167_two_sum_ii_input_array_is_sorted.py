"""167. Two Sum II - Input Array Is Sorted のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
昇順に並んだ配列から、足して target になる 2 つの位置を **1 始まり**で返す。答えはちょうど 1 組。
"""

import random


def test_example_1(solution):
    assert solution.Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]


def test_example_2(solution):
    assert solution.Solution().twoSum([2, 3, 4], 6) == [1, 3]


def test_example_3(solution):
    assert solution.Solution().twoSum([-1, 0], -1) == [1, 2]


def test_same_values(solution):
    # 同じ値の 2 つを使う
    assert solution.Solution().twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]


def test_answer_at_both_ends(solution):
    assert solution.Solution().twoSum([1, 5, 6, 7, 100], 101) == [1, 5]


def test_random_against_brute_force(solution):
    rng = random.Random(167)
    for _ in range(300):
        n = rng.randint(2, 30)
        nums = sorted(rng.sample(range(-200, 200), n))
        i, j = sorted(rng.sample(range(n), 2))
        target = nums[i] + nums[j]
        # 答えが 1 組だけになる入力に限る
        pairs = [(a, b) for a in range(n) for b in range(a + 1, n) if nums[a] + nums[b] == target]
        if len(pairs) != 1:
            continue
        a, b = pairs[0]
        assert solution.Solution().twoSum(nums, target) == [a + 1, b + 1]
