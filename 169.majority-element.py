#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        ans = nums[0]
        freq[ans] = 1
        for n in nums[1:]:
            freq[n] = freq.get(n, 0) + 1
            if freq[n] > freq[ans]:
                ans = n
        return ans

    def optimalSolution(self, nums: List[int]) -> int:
        lead = 0
        ans = nums[0]
        for i in range(len(nums)):
            # update leading number
            if lead == 0:
                ans = nums[i]
            if ans == nums[i]:
                lead += 1
            else:
                lead -= 1
        return ans


# @lc code=end
