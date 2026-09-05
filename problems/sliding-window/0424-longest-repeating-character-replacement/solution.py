"""424. Longest Repeating Character Replacement

https://leetcode.com/problems/longest-repeating-character-replacement/
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initialize window state (a hashmap that stores the frequencies of each character)
        map = {}
        # initialize result variable (the length of the longest substring)
        res = 0
        # initialize left pointer
        left = 0

        # iterate right pointer from left to right:
        for right in range(len(s)):
            # add right element to window (update hashmap)
            map[s[right]] = map.get(s[right], 0) + 1

            # find the frequency of most frequent character
            maxFrequency = max(map.values())

            # while total number of occurrences of all characters except for most frequent one is more than k:
            while k < len(s[left:right + 1]) - maxFrequency:
                print("while")
                # remove left character from hashmap (update hashmap)
                map[s[left]] = map.get(s[left]) - 1
                # move left pointer forward (remove left character from window)
                left += 1

            # update result (max window length)
            res = max(res, right - left + 1)

        # return result (max window length)
        return res
