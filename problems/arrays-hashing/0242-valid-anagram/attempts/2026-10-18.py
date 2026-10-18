"""242. Valid Anagram

https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        maps = {}
        mapt = {}

        for c in s:
            if c in maps:
                maps[c] += 1
            else:
                maps[c] = 0

        for c in t:
            if c in mapt:
                mapt[c] += 1
            else:
                mapt[c] = 0

        return maps == mapt
