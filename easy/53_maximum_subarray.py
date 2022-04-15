# Easy
# O(n)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        highest_score=nums[0]
        current_sum = 0
        for i in nums:
            current_sum+=i
            
            if (current_sum > highest_score):
                highest_score = current_sum
                
            if (current_sum<0):
                current_sum = 0
        return highest_score

# Method2: divide and conquer
