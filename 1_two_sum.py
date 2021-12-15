# Easy
# O(n)?
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [i,d[m]]
            else:
                d[n]=i