#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#

# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # sorted potions first, so for each spell, 
        # we only have to find the first product that is larger than success
        # how to find the first number? use binary search
        potions = sorted(potions)
        n = len(potions)
        res = []
        for s in spells:
            threshold = success/s
            # binary search
            theFirstValidPotionIdx = self.binarySearch(potions, threshold)
            res.append(n-theFirstValidPotionIdx)
        return res

    def binarySearch(self, array, key):
        # return the leftmost item that's equal or larger than key
        l, r = 0, len(array)-1
        while l<=r:
            mid = (l+r)//2
            if (array[mid])>=key:
                r = mid- 1
            else:
                l = mid+ 1
        return l
    
# @lc code=end

