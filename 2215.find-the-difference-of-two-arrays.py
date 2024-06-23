#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#


# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # parse two array and produce two sets
        set1 = set()
        set2 = set()
        for n in nums1:
            set1.add(n)
        for n in nums2:
            set2.add(n)
        ans = [[], []]
        for n in set1:
            if n not in set2:
                ans[0].append(n)
        for n in set2:
            if n not in set1:
                ans[1].append(n)
        return ans


# @lc code=end
