"""20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if c == ')' and stack != [] and stack.pop() == '(':
                    continue
                elif c == '}' and stack != [] and stack.pop() == '{':
                    continue
                elif c == ']' and stack != [] and stack.pop() == '[':
                    continue
                else:
                    return False

        if stack == []:
            return True
        else:
            return False
