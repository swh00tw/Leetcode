#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#


# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window
        # use a var to keep track of best answer
        # first, have k chances to ignore zero and keep counting
        # if encounter next zero, need to move left pointer to the right of first zero it encounters
        # (recycling the chance to ignore zero)
        n = len(nums)
        chances = k
        left = 0
        best = 0
        for right in range(n):
            num = nums[right]
            if num == 0:
                if chances == 0:
                    # recycle, move left
                    while left <= right:
                        if nums[left] == 0:
                            break
                        left += 1
                    left += 1
                else:
                    chances -= 1
            best = max(best, right + 1 - left)
        return best


# @lc code=end
