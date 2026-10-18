"""125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1

        while l < r:
            # move left pointer inward until the character is alphabet or digit
            while l < r and not s[l].isalnum():
                l += 1

            # move right pointer inward until the character is alphabet or digit
            while l < r and not s[r].isalnum():
                r -= 1

            # check if the characters at left and right pointers are the same in lowercase
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
