#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]+[0]*n
        power = 0
        for i in range(1, n+1):
            if i==2**(power+1):
                ans[i] = 1
                power += 1
            else:
                ans[i] = 1+ans[i-2**power]
        return ans
    
# 0 0
# 1 1
# 2 10
# 3 11
# 4 100
# 5 101
# 6 110
# 7 111
# 8 1000
# 9 1001
# 10 1010

        
# @lc code=end

