#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
# ref: https://leetcode.com/problems/increasing-triplet-subsequence/solutions/2688195/python-3-6-lines-one-pass-w-explanation-t-m-98-50/
# if there's a "second" != inf, it means there must be a number located in the front and value < second
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        first, second = inf, inf
        
        for third in nums:
            if second < third: return True
            if third <= first: first= third    
            else:  second = third 
                
        return  False
                    


# @lc code=end

