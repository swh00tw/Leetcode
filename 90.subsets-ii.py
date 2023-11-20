#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
from collections import Counter


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort the number
        # use a hashmap: freq to count the freq of each number
        # remove duplicates from nums

        # recursive function, getSubsets(idx) -> List[List[int]]
        # use nums[idx] insert in front of getSubsets(idx+1) --> check freq[nums[idx]] -> we can use 0, 1, 2, ..., freq[nums[idx]]

        # base case: idx >= len(nums):
        # return []

        nums.sort()
        freq = Counter(nums)
        new_nums = []
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
                new_nums.append(num)
        nums = new_nums

        def getSubsets(idx):
            if idx == len(nums) - 1:
                res = []
                for n in range(freq[nums[idx]] + 1):
                    res.append([nums[idx]] * n)
                return res

            subsets = getSubsets(idx + 1)
            res = []
            for subset in subsets:
                for n in range(freq[nums[idx]] + 1):
                    res.append([nums[idx]] * n + subset)
            return res

        return getSubsets(0)


# @lc code=end
