"""15. 3Sum

https://leetcode.com/problems/3sum/
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if [nums[i], nums[j], nums[k]] not in triplets and [nums[i], nums[k], nums[j]] not in triplets and [nums[j], nums[i], nums[k]] not in triplets and [nums[j], nums[k], nums[i]] not in triplets and [nums[k], nums[i], nums[j]] not in triplets and [nums[k], nums[j], nums[i]] not in triplets:
                            triplets.append([nums[i], nums[j], nums[k]])

        return triplets
