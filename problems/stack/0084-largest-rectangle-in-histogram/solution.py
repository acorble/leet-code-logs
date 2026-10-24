"""84. Largest Rectangle in Histogram

https://leetcode.com/problems/largest-rectangle-in-histogram/
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            newPositionLeft = i
            # if current height is lower than stack[-1]
            while stack and h < stack[-1][0]:
                # pop from the stack
                heightLeft, positionLeft = stack.pop()
                # compute the area with popped height and update maxArea
                maxArea = max(maxArea, heightLeft * (i - positionLeft))
                # update position that will be pushed onto stack
                newPositionLeft = positionLeft

            # push current height and position onto stack
            stack.append((h, newPositionLeft))

        while stack:
            # pop from the stack
            heightLeft, positionLeft = stack.pop()
            # compute the area with popped height and update maxArea
            maxArea = max(maxArea, heightLeft * (len(heights) - positionLeft))

        return maxArea
