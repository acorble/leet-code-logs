"""153. Find Minimum in Rotated Sorted Array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search solution

        # check if nums is sorted monotonically
        if nums[0] < nums[len(nums) - 1]:
            # if so, first element is the least number
            # return result (first element)
            return nums[0]
        # otherwise, the least number lies between second and n position
        else:
            # initialize left and right pointer to deifine search space
            l, r = 0, len(nums) - 1
            # initialize variable to store temporary minimum number
            minimum = None
            # while loop: while left < right
            while l <= r:
                # calculate middle pointer
                m = l + (r - l) // 2
                # print(f"l:{l}, r:{r}, m:{m}")
                # check if middle nubmer is greater than last number
                if nums[m] <= nums[len(nums) - 1]:
                    # if smaller, search in the left half next
                    minimum = nums[m]
                    r = m - 1
                # if greater, search in the right half next
                else:
                    l = m + 1

            # return result
            return minimum
