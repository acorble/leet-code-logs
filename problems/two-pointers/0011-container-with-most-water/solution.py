"""11. Container With Most Water

https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # set initial two pointers to the left and right ends
        left, right = 0, len(height) - 1

        # initialize the maximum amount of water
        max = 0

        # calculate the initial maximum
        if height[0] < height[len(height) - 1]:
            max = (len(height) - 1) * height[0]
        else:
            max = (len(height) - 1) * height[len(height) - 1]

        # while loop until the two pointers meet
        while left < right:
            # if the left line is shorter:
            if height[left] < height[right]:
                originalShorterHeight = height[left]

                # while loop
                while left < right:
                    # increment left poniter
                    left += 1
                    # if the new line is higher than the original one, exit the while loop
                    if originalShorterHeight < height[left]:
                        break

                # calculate the new amount of water
                newAmount = 0
                if height[left] < height[right]:
                    newAmount = (right - left) * height[left]
                else:
                    newAmount = (right - left) * height[right]

                # if the new one is bigger, update the maximum
                if max < newAmount:
                    max = newAmount
            # if the right line is shorter:
            else:
                originalShorterHeight = height[right]

                # while loop
                while left < right:
                    # decrement right poniter
                    right -= 1
                    # if the new line is higher than the original one, exit the while loop
                    if originalShorterHeight < height[right]:
                        break

                # calculate the new amount of water
                newAmount = 0
                if height[left] < height[right]:
                    newAmount = (right - left) * height[left]
                else:
                    newAmount = (right - left) * height[right]

                # if the new one is bigger, update the maximum
                if max < newAmount:
                    max = newAmount
        # return the maximum
        return max
