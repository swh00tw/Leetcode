#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        res = []
        a, b = nums[0], nums[0]
        for num in nums[1:]:
            if num == b + 1:
                b = num
            else:
                res.append(f"{a}->{b}" if a!=b else str(a))
                a, b = num, num
        res.append(f"{a}->{b}" if a!=b else str(a))
        return res
        
        
# @lc code=end

