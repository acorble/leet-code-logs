"""20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # initialize stack
        stack = []

        # iterate through string
        for c in s:
            # if character is equal to '(', '{' or '['
            if c == '(' or c == '{' or c == '[':
                # append the character to stack
                stack.append(c)

            # if character is equal to ')', '}' or ']':
            else:
                # get stack[-1]
                if stack:
                    a = stack[-1]
                else:
                    return False

                # if close bracket is correspoinding one of popped open bracket:
                if c == ')' and a == '(':
                    # pop stack
                    if stack:
                        stack.pop()
                elif c == '}' and a == '{':
                    if stack:
                        stack.pop()
                elif c == ']' and a == '[':
                    if stack:
                        stack.pop()
                # else:
                else:
                    # return false
                    return False

        # return true
        if not stack:
            return True
        else:
            return False
