#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        fib = [0, 1]
        if n == 0 or n==1:
            return fib[n]
        else:
            for i in range(2, n+1):
                fib.append(fib[i-1]+fib[i-2])
            return fib[-1]
        
# @lc code=end

