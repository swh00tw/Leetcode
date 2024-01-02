#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#


# @lc code=start
class Node:
    def __init__(self, val, currMin):
        self.val = val
        self.min = currMin


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        currMin = self.stack[-1].min if len(self.stack) > 0 else val
        node = Node(val, min(currMin, val))
        self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
