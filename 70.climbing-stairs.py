#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        ways = [0]*(n+1)
        ways[1]=1
        ways[2]=1
        for i in range(1, n+1):
            ways[i]+=ways[i-1] if i-1>=0 else 0
            ways[i]+=ways[i-2] if i-2>=0 else 0
        return ways[n] 
        
# @lc code=end

