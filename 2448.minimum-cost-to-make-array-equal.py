#
# @lc app=leetcode id=2448 lang=python3
#
# [2448] Minimum Cost to Make Array Equal
#

# @lc code=start
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        self.cost = cost
        self.nums = nums
        minNumber = min(nums)
        maxNumber = max(nums)
        if minNumber == maxNumber:
            return 0
        l, r = minNumber, maxNumber
        while l<=r:
            mid = (l+r)//2
            midCost = self.getCost(mid)
            midLeftCost = self.getCost(mid-1)
            midRightCost = self.getCost(mid+1)
            if midLeftCost>=midCost and midRightCost>=midCost:
                return midCost
            if midLeftCost<midCost<midRightCost:
                r = mid-1
            elif midLeftCost>midCost>midRightCost:
                l =mid+1
        
    def getCost(self, x):
        res = 0
        for num, c in list(zip(self.nums, self.cost)):
            res += c*abs(x-num)
        return res

        
# @lc code=end

