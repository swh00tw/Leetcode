#
# @lc app=leetcode id=1406 lang=python3
#
# [1406] Stone Game III
#

# @lc code=start
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp problem
        # we create a 1d table to store the best score one can get starting from each position
        # we also need to keep track of the choice of taking 1 or 2 or 3 from each position
        # we create a suffixSum array first to reduce tht time complexity
        n = len(stoneValue)
        dp = [0]*n
        choice = [0]*n
        suffixSum = [0]*n
        for i in range(n-1, -1, -1):
            suffixSum[i] = stoneValue[i]+(suffixSum[i+1] if i+1<n else 0)
        
        for startIndex in range(n-1, -1, -1):
            choose1 = (suffixSum[startIndex]-(dp[startIndex+1] if startIndex+1<n else 0), 1)
            choose2 = (-inf if startIndex>n-2 else suffixSum[startIndex]-(dp[startIndex+2] if startIndex+2<n else 0), 2)
            choose3 = (-inf if startIndex>n-3 else suffixSum[startIndex]-(dp[startIndex+3] if startIndex+3<n else 0), 3)
            bestChoice = max([choose1, choose2, choose3], key=lambda x:x[0])
            dp[startIndex] = bestChoice[0]
            choice[startIndex] = bestChoice[1]
        alice = dp[0]
        bob = dp[choice[0]] if choice[0]<n else 0 
        return "Tie" if alice==bob else ("Alice" if alice>bob else "Bob")
            
        
# @lc code=end

