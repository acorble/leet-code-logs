"""167. Two Sum II - Input Array Is Sorted

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize two pointers, left and right
        left, right = 0, len(numbers) - 1

        # while loop until numbers[left] + numbers[right] is not target and left < right
        while left < right and numbers[left] + numbers[right] != target:
            # if the sum of numbers[left] and numbers[right] < target, increment left
            if numbers[left] + numbers[right] < target:
                left += 1
            # if the sum of numbers[left] and numbers[right] > target, decrement right
            elif target < numbers[left] + numbers[right]:
                right -= 1

        # return result
        return [left + 1, right + 1]
