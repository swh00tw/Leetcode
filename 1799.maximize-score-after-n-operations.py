#
# @lc app=leetcode id=1799 lang=python3
#
# [1799] Maximize Score After N Operations
#

# @lc code=start
# ref: https://leetcode.com/problems/maximize-score-after-n-operations/solutions/3521561/python-java-c-simple-solution-easy-to-understand/
from math import gcd
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        gcd_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                gcd_matrix[i][j] = gcd_matrix[j][i] = gcd(nums[i], nums[j])
        
        # each index number map to a bit mask and map to the subset of nums
        # and each index store the maximum possible value
        # ex: if nums = [3, 4, 6, 8], 
        # 0 --> [0, 0, 0, 0] --> the optimal answer for []
        # 1 --> [0, 0, 0, 1] 
        # 2 --> [0, 0, 1, 0]
        # 3 --> [0, 1, 0, 1] --> the optimal answer for [4, 8]
        # 4 --> [0, 1, 1, 0] --> the optimal answer for [4, 6]
        # 15 --> [1, 1, 1, 1] --> the optimal answer for [3, 4, 6, 8]
        dp = [0] * (1 << n)
        

        for state in range(1, 1 << n):
            cnt = bin(state).count('1')
            if cnt % 2 == 1:
                continue
            
            
            for i in range(n):
                # if after AND operation the number is 0, continue
                if not (state & (1 << i)):
                    continue
                for j in range(i+1, n):
                    # if after AND operation the number is 0, continue
                    if not (state & (1 << j)):
                        continue
                    # subproblem's state
                    nextState = state ^ (1 << i) ^ (1 << j)
                    dp[state] = max(dp[state], dp[nextState] + cnt // 2 * gcd_matrix[i][j])
        
        return dp[(1 << n) - 1]
        
# @lc code=end

