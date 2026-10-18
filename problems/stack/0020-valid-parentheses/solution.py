"""20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False

        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if stack == []:
                    return False
                else:
                    c2 = stack.pop()
                if c == ')':
                    if c2 != '(':
                        return False
                elif c == '}':
                    if c2 != '{':
                        return False
                elif c == ']':
                    if c2 != '[':
                        return False

        if stack == []:
            return True
        else:
            return False
