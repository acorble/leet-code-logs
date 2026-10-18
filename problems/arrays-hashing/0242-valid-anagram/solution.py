"""242. Valid Anagram

https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        maps, mapt = {}, {}

        for c in s:
            maps[c] = maps.get(c, 0) + 1

        for c in t:
            mapt[c] = mapt.get(c, 0) + 1

        return maps == mapt
