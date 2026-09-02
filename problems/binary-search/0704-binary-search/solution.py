"""704. Binary Search

https://leetcode.com/problems/binary-search/
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        middle = int(len(nums) / 2)
        left, right = 0, len(nums) - 1

        while 1 < right - left:
            print(f"middle: {middle}")

            if target < nums[middle]:
                print("left")
                right = middle
                middle = left + int((right - left) / 2)
            elif nums[middle] < target:
                print("right")
                left = middle
                middle = left + int((right - left) / 2)
            else:
                return middle

        if target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        else:
            return -1
