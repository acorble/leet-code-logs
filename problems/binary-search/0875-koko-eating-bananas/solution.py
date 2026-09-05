"""875. Koko Eating Bananas

https://leetcode.com/problems/koko-eating-bananas/
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k * h > sum of piles[i]
        numberOfBananas = range(1, max(piles) + 1)
        left, right = 0, len(numberOfBananas) - 1

        while left < right:
            m = left + (right - left) // 2
            k = numberOfBananas[m]
            # print(f"left={left}({numberOfBananas[left]}), m={m}({k}), right={right}({numberOfBananas[right]})")
            if self.ifFinishEating(piles, h, k):
                right = m
            else:
                left = m + 1
            # print()
        return numberOfBananas[left]

    def ifFinishEating(self, piles, h, k) -> bool:
        eatingHour = 0

        for pile in piles:
            if pile % k == 0:
                eatingHour += (pile // k)
            else:
                eatingHour += (pile // k) + 1

        if eatingHour <= h:
            return True
        else:
            return False
