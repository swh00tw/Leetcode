# medium
# O(n^2)
# 2 sum: O(n)
# The problem can be reduced to a for loop of 2 sum problem after sorted.
# BUT! need to handle the duplicated answers
# ref: https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanation

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]: # because the pivor number nums[i] has already been inspected, so we skip it
                continue
            target = nums[i]*-1 # target of 2 sum problem
            s,e = i+1, N-1 # this is the searching area
            while s<e:
                if nums[s]+nums[e] == target:
                    # match!
                    result.append([nums[i], nums[s], nums[e]])
                    # keep searching for other matches using the same pivor number
                    s = s+1
                    # avoid duplicates answers, move left pointer forward if nums[s] == nums[s-1], ( nums[s] duplicated )
                    while s<e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < target: # it means we need to increase the left pointer to make a larger sum to meet the target
                    s = s+1
                else: # it means we need to decrease the right pointer to make a smaller sum to meet the target
                    e = e-1
        return result