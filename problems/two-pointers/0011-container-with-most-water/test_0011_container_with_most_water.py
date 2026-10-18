"""11. Container With Most Water のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
2 本の線を選んで、その間に溜められる水の量（幅 × 低いほうの高さ）の最大を返す。
"""

import random


def brute_force(height):
    n = len(height)
    return max((j - i) * min(height[i], height[j]) for i in range(n) for j in range(i + 1, n))


def test_example_1(solution):
    assert solution.Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_2(solution):
    assert solution.Solution().maxArea([1, 1]) == 1


def test_zero_heights(solution):
    assert solution.Solution().maxArea([0, 0, 0]) == 0


def test_increasing(solution):
    # 両端（幅 4 × 高さ 1 = 4）より、高さ 2 と 5（幅 3 × 2）や 3 と 5（幅 2 × 3）の 6 のほうが大きい
    assert solution.Solution().maxArea([1, 2, 3, 4, 5]) == 6


def test_random_against_brute_force(solution):
    rng = random.Random(11)
    for _ in range(500):
        height = [rng.randint(0, 10) for _ in range(rng.randint(2, 15))]
        assert solution.Solution().maxArea(height) == brute_force(height), height
