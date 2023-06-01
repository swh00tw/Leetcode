#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k-1
        curr = sum(nums[l:r+1])
        best = curr
        l += 1
        r += 1
        while r<len(nums):
            curr = curr - nums[l-1] + nums[r]
            best = max(best, curr)
            r+=1
            l+=1
        return best/k
        
# @lc code=end

