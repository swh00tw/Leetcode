#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#


# @lc code=start
class MyQueue:
    def __init__(self):
        # 1. maintain a pointer to point to the oldest element in the stack
        # to achieve O(1) time peek
        # 2. and a stack
        # 3. pop will take O(n) depend on the number of elements in the stack
        # but, before you perform pop and take O(n), there must be n times push,
        # so amortizedly, n+1 operations take O(n) time, the amortized time complexity
        # is O(1)
        self.oldest = None
        self.stack = []
        self.helperStack = []

    def push(self, x: int) -> None:
        # O(1)
        if len(self.stack) == 0:
            self.oldest = x
        self.stack.append(x)

    def pop(self) -> int:
        # O(n)
        # offload everything except the last one to another stack
        # get the last one
        # load everything back to stack
        # return
        while not self.empty():
            self.helperStack.append(self.stack.pop())
        target = self.helperStack.pop()
        self.oldest = self.helperStack[-1] if len(self.helperStack) > 0 else None
        while len(self.helperStack) > 0:
            self.stack.append(self.helperStack.pop())
        return target

    def peek(self) -> int:
        # O(1)
        return self.oldest

    def empty(self) -> bool:
        # O(1)
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
