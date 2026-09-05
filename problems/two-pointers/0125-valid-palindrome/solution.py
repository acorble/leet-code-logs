"""125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize two pointers (left and right)
        left, right = 0, len(s) - 1

        # while loop until two pointers meet
        while left < right:
            # while loop (left pointer)
            while left < right:
                # check if the character is alphanumeric
                if s[left].isalnum():
                    # if true: exit loop
                    break
                # if false: increment left pointer
                else:
                    left += 1
            # while loop (right pointer)
            while left < right:
                # check if the character is alphanumeric
                if s[right].isalnum():
                    # if true: exit loop
                    break
                # if false: decrement right pointer
                else:
                    right -= 1
            # check if the two characters at both pointers differ (case-insensitive)
            if s[left].lower() != s[right].lower():
                # return False
                return False
            # move both pointers inward
            left += 1
            right -= 1

        return True
