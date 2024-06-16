#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#


# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window
        # keep track of current average and best average
        n = len(nums)
        curr_avg = 0
        for i in range(k):
            curr_avg += nums[i] / k
        if n == k:
            return curr_avg
        best_avg = curr_avg
        for i in range(k, n):
            curr_avg -= nums[i - k] / k
            curr_avg += nums[i] / k
            best_avg = max(best_avg, curr_avg)
        return best_avg


# @lc code=end
