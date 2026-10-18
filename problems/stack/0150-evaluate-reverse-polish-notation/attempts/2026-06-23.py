"""150. Evaluate Reverse Polish Notation（2026-06-23 の解答）

https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # initialize result
        res = 0

        # while loop: until length of tokens is 1
        while len(tokens) > 1:
            previous = None

            # iterate through tokens for each element
            for i, s in enumerate(tokens):
                # check if each string represents number or operator
                if self.checkIfInteger(s):
                    # if two numbers exist in a row
                    if previous is not None and self.checkIfInteger(previous):
                        if not self.checkIfInteger(tokens[i + 1]):
                            # initialize next operator
                            next = tokens[i + 1]
                            # initialize calculated value
                            value = 0

                            # calculate by RPN
                            if next == '+':
                                value = int(s) + int(previous)
                            elif next == '-':
                                value = int(previous) - int(s)
                            elif next == '*':
                                value = int(s) * int(previous)
                            else:
                                value = int(int(previous) / int(s))

                            # replace the two numbers with result of calculation (1 2 + -> 3)
                            tokens.insert(i + 2, value)
                            tokens.pop(i - 1)
                            tokens.pop(i - 1)
                            tokens.pop(i - 1)

                            # exit for loop
                            break

                    previous = int(s)
                else:
                    previous = s

        if len(tokens) == 1:
            res = int(tokens[0])

        # return result
        return res

    def checkIfInteger(self, s) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False
