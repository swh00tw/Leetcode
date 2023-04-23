#
# @lc app=leetcode id=1416 lang=python3
#
# [1416] Restore The Array
#

# @lc code=start
# ref: https://leetcode.com/problems/restore-the-array/solutions/3445400/python-java-c-simple-solution-easy-to-understand/
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n+1) # dp[i] is the answer for s[i:n]
        dp[-1] = 1 # since there is only one way for s[n:n] (empty string)

        for i in range(n-1, -1, -1): # backward
            num = int(s[i])
            if num == 0:
                continue
            
            ways = 0
            j = i
            while j<n and int(s[i:j+1])<=k:
                ways += dp[j+1]
                j+=1
            dp[i] = ways
        return dp[0]%(10**9+7)



# @lc code=end

