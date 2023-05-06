#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#

# @lc code=start
# ref: https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/editorial/
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # sorted the nums first
        # maintain 2 pointers: left, right
        # traverse all possible minimum of all subseq (by left pointer)
        # move right pointer to the index so that nums[left]+nums[right]<=target
        # the all "valid" subseq that start from left index is 2^(right-left)
        n = len(nums)
        nums.sort()

        ans = 0
        left = 0
        right = n-1
        while left<=right:
            if nums[left]+nums[right]<=target:
                ans= (ans + 2**(right-left)) % (10**9+7)
                left+=1
            else:
                right-=1
        return ans%(10**9+7)
        
# @lc code=end

