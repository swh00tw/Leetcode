#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # two pointers, keep counting acc 1s
        # if encounter 1, increment and move right pointer
        # if encounter 0 and have chance, skip
        # if encounter 0 and don't have chance, restore the chance we used before (update left pointer to its right)
        chance = True
        acc = 0
        best = 0
        l, r=0, 0
        while r<len(nums):
            if nums[r]==1:
                r += 1
                acc += 1
            elif nums[r]==0 and chance:
                chance = not chance
                r+=1
            else:
                # save best score now
                best = max(best, acc)
                # move l to the first 0's right
                while l<len(nums):
                    if nums[l]==1:
                        acc-=1
                    elif nums[l]==0:
                        l+=1
                        break
                    l+=1
                r+=1
        best = max(best, acc)
        return best-1 if chance else best

                
        
# @lc code=end

