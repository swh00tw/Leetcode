#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    def __init__(self):
        self.s = [] # stack
        self.min = float("inf")

    def push(self, val: int) -> None:
        self.s.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        top = self.top()
        self.s.pop(-1)        
        if top == self.min:
            self.min = min(self.s) if self.s else float("inf")

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min
# True O(1) answer here!
# ref: https://leetcode.com/problems/min-stack/solutions/3297934/python-one-stack-without-tuples-and-linklist/?languageTags=python3



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

