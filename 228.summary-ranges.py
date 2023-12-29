#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [f"{nums[0]}"]
        intervals = []  # [a, b]
        curr = [nums[0], nums[0]]
        for n in nums[1:]:
            if n == curr[1] + 1:
                curr = [curr[0], n]
            else:
                intervals.append(curr)
                curr = [n, n]
        intervals.append(curr)
        return [f"{a}->{b}" if a != b else f"{a}" for a, b in intervals]


# @lc code=end
