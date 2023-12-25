#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # create a tmp array that store nums1[:m]
        # two pointers, keep picking the smaller one, fill the nums1
        tmp = nums1[:m]
        p1, p2 = 0, 0
        i = 0
        while p1 < m or p2 < n:
            n1 = tmp[p1] if p1 < m else float("inf")
            n2 = nums2[p2] if p2 < n else float("inf")
            if n1 < n2:
                nums1[i] = n1
                p1 += 1
                i += 1
            else:
                nums1[i] = n2
                p2 += 1
                i += 1


# @lc code=end
