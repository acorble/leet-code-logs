"""739. Daily Temperatures

https://leetcode.com/problems/daily-temperatures/
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = []

        for i, temp in enumerate(temperatures):
            print(i, temp)
            print(range(i + 1, len(temperatures) - 1))
            for j in range(i + 1, len(temperatures)):
                # print(temp)
                if temp < temperatures[j]:
                    ans.append(j - i)
                    break
            if len(ans) - 1 != i:
                ans.append(0)

        return ans
