"""567. Permutation in String

https://leetcode.com/problems/permutation-in-string/
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create hashmap to store character counts
        s1map = {}
        s2map = {}
        l = 0

        for c in range(len(s1)):
            if s1[c] not in s1map:
                s1map[s1[c]] = 0
            s1map[s1[c]] += 1

        for r in range(len(s2)):
            print(f"l = {l}, r = {r}")
            if s2[r] not in s1map:
                l = r + 1
                s2map = {}
                continue

            if s2[r] not in s2map:
                s2map[s2[r]] = 0
            s2map[s2[r]] += 1

            while s1map[s2[r]] < s2map[s2[r]]:
                s2map[s2[l]] -= 1
                l += 1

            if s1map == s2map:
                return True

        return False
