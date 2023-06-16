#
# @lc app=leetcode id=1569 lang=python3
#
# [1569] Number of Ways to Reorder Array to Get Same BST
#

# @lc code=start
from math import comb
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        # recursive problem
        ans = self.getNumOfWays(nums)
        return (ans-1)%(10**9+7)
    
    def getNumOfWays(self, nums):
        # recursive problem
        n = len(nums)
        if n<=2:
            return 1
        root = nums[0]
        leftSubtreeNums, rightSubtreeNums = [], []
        for num in nums[1:]:
            if num<root:
                leftSubtreeNums.append(num)
            else:
                rightSubtreeNums.append(num)
        leftNumOfWays = self.getNumOfWays(leftSubtreeNums)
        rightNumOfWays = self.getNumOfWays(rightSubtreeNums)
        positionCombination = comb(n-1, len(leftSubtreeNums))
        return positionCombination * leftNumOfWays * rightNumOfWays
        

 
        
        
# @lc code=end

