"""155. Min Stack

https://leetcode.com/problems/min-stack/
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minArr = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.minArr:
            self.minArr.append(min(self.minArr[-1], value))
        else:
            self.minArr.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minArr.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minArr[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
