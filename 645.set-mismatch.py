#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#


# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_set = set([x + 1 for x in range(len(nums))])
        ans = [0, 0]
        for n in nums:
            if n in nums_set:
                nums_set.discard(n)
            else:
                ans[0] = n
        ans[1] = nums_set.pop()
        return ans


# @lc code=end
