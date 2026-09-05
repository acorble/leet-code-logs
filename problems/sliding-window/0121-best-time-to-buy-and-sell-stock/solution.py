"""121. Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set two pointers (left = 0, right = 1)
        left, right = 0, 1
        # set max profit to 0
        maxProfit = 0

        # while loop
        while right < len(prices):
            # if the price at right (sell day) is higher than left (buy day)
            if prices[left] < prices[right]:
                # if the profit is higher than the previous max profit, update the max profit
                maxProfit = max(maxProfit, prices[right] - prices[left])

            # otherwise, update the buy day (update left to right)
            else:
                left = right
            # increment right
            right += 1

        # return max profit
        return maxProfit
