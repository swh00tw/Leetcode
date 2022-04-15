# easy
# O(n)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums==[]:
            return 0
        newTail=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[newTail]=nums[i]
                newTail+=1
        return newTail