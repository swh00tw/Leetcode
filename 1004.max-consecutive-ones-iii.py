#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # two pointers
        # traverse thru nums
        # if encounter zero, spent a chance of fliping on it
        # keep track of maximum length of consecutive 1s
        # if we spent all chances and encounter zero,
        # the left pointer should move to the right of first zero we spent our chance on
        # move left pointer to the right of first flipping zero, (keep minus acc by 1)
        l, r = 0, 0
        acc = 0
        best = 0
        chances = k
        while r<len(nums):
            if nums[r] == 0 and chances>0:
                chances -= 1
            elif nums[r]==0 and chances==0:
                # save best score
                best = max(best, acc)
                # recalculate acc
                while l<len(nums):
                    acc -= 1
                    if nums[l]==0:
                        l = l+1
                        break
                    l += 1
            acc += 1
            r += 1
        best = max(best, acc)
        return best
            
# @lc code=end

