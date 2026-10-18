"""217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            else:
                s.add(n)
        return False
