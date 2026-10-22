"""739. Daily Temperatures

https://leetcode.com/problems/daily-temperatures/
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                minimum = stack.pop()
                ans[minimum[1]] = i - minimum[1]
            stack.append((t, i))

        return ans
