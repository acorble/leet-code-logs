"""15. 3Sum

https://leetcode.com/problems/3sum/
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sort nums in ascending order
        nums.sort()
        # print(f"sorted nums = {nums}")
        # print("\n")
        
        # initialize result array
        result = []

        previousFirstNumber = None

        # for loop (fix the first pointer)
        for i in range(len(nums) - 2):
            print(f"i, nums[i] = {i}, {nums[i]}")
            if nums[i] != previousFirstNumber:
                # initialize two pointers, left and right
                # set left pointer to next number of the first pointer
                # set right pointer to the biggest number
                left, right = i + 1, len(nums) - 1

                # while loop until left < right
                while left < right:
                    # print(f"i={i}, nums[i] = {nums[i]}")
                    # print(f"left={left}, nums[left] = {nums[left]}")
                    # print(f"right={right}, nums[right] = {nums[right]}\n")

                    # if the sum of the 3 numbers < 0, increment left pointer
                    if nums[i] + nums[left] + nums[right] < 0:
                        left += 1
                    # if the sum of the 3 numbers > 0, decrement right pointer
                    elif 0 < nums[i] + nums[left] + nums[right]:
                        right -= 1
                    # if the sum of the 3 numbers = 0, add the array of the 3 numbers to result array
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        # print("appended")

                        left += 1
                        right -= 1
                        # print(f"next left={left}, next right = {right}")
                        # print(f"nums[left - 1]={nums[left - 1]}")
                        # print(f"nums[left]={nums[left]}")
                        # print(f"nums[right + 1]={nums[right + 1]}")
                        # print(f"nums[right]={nums[right]}")

                        while nums[left - 1] == nums[left] and nums[right + 1] == nums[right] and left < right:
                            left += 1
                            right -= 1

            previousFirstNumber = nums[i]
        # if there are duplicates in result array, remove them
        
        # return result array
        return result
