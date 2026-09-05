"""3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set left pointer to 0, right pointer to 1
        left, right = 0, 1
        # set max substring length to 0
        maxLength = 0
        # initialize hashset to check if duplicate exists
        charSet = set()

        if len(s) > 0:
            charSet.add(s[0])
            maxLength = 1

        # while loop until right pointer reaches the rightmost
        while right < len(s):
            # if the rightmost character does not exist in the window:
            if s[right] not in charSet:
                # update the max length
                maxLength = max(maxLength, right - left + 1)

                # add the new character to hashset
                charSet.add(s[right])

            # if the character at right already exists in the window
            else:
                # find the duplicated character
                duplicated = s[left:right].index(s[right])

                # remove characters in the substring between left pointer and duplicated character found earlier from hashset
                i = 0
                while s[right] in charSet:
                    charSet.remove(s[left + i])
                    i += 1

                # add the new character to hashset
                charSet.add(s[right])

                # update left
                left = left + duplicated + 1

            # increment right pointer
            right += 1

        # return max length as a result
        return maxLength
