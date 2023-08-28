#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#


# @lc code=start
class MyStack:
    def __init__(self):
        self.main = []  # queue
        self.tmp = []  # queue

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        ans = None
        while True:
            val = self.main.pop(0)
            if not self.main:
                ans = val
                break
            else:
                self.tmp.append(val)
        self.main = self.tmp[:]
        self.tmp = []

        return ans

    def top(self) -> int:
        ans = None
        while self.main:
            val = self.main.pop(0)
            self.tmp.append(val)
            if not self.main:
                ans = val
        self.main = self.tmp[:]
        self.tmp = []

        return ans

    def empty(self) -> bool:
        return len(self.main) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
