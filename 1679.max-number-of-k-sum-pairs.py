#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        i, j = 0, n-1
        c = 0
        while i<j:
            if len(nums)<=1:
                break
            if nums[i]+nums[j]==k:
                nums.pop(j)
                nums.pop(i)
                j = j-2
                c+=1
            elif nums[i]+nums[j]>k:
                j -=1
            else:
                i+=1
        return c
        
# @lc code=end

