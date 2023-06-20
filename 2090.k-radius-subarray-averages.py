#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1]*n
        windowSize = 0 # max size is 2k+1
        windowSum = 0 
        maxSize = 2*k+1
        for i in range(n):
            if windowSize == maxSize:
                windowSum -= nums[i-maxSize]
            else:
                windowSize+=1
            windowSum += nums[i]

            if windowSize == maxSize:
                res[i-k] = windowSum//(2*k+1)
        return res
        
# @lc code=end

