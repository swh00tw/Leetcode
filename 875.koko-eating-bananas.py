#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # first, need to notice the range of possible answer k is in [1, max(piles)]
        # then apply binary search to find the rightmost k that meet the restriction(finish in given h)
        rangeOfk = [1, max(piles)]
        l, r = rangeOfk
        while l<=r:
            mid = (l+r)//2
            # calculate total hrs needed
            totalHoursNeeded = 0
            for p in piles:
                totalHoursNeeded += math.ceil(p/mid)
            
            if totalHoursNeeded <= h:
                # search lower half to see if we can find better k
                r = mid -1
            else:
                # search upper half
                l = mid +1
        return l
        
# @lc code=end

