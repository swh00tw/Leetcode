#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # sol: https://www.youtube.com/watch?v=q6IEA26hvXc

        # find the right partition on nums1 and nums2
        # use binary search on nums1
        # verify if it's valid partition
        # handle odd case and even case

        # KEY: assume nums1 is always smaller, nums2 is bigger
        # though not affect the correctness,
        # by doing so, we won't have "list-out-of-range" issue
        # we don't have to handle these cases
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)
        total = n + m
        targetParitionLength = total // 2

        l, r = 0, n
        while l <= r:
            break1 = (l + r) // 2
            break2 = targetParitionLength - break1

            # verify partition
            right1 = nums1[break1] if break1 < n else float("inf")
            right2 = nums2[break2] if break2 < m else float("inf")
            left1 = nums1[break1 - 1] if (break1 - 1 >= 0) else float("-inf")
            left2 = nums2[break2 - 1] if (break2 - 1 >= 0) else float("-inf")
            if left1 <= right2 and left2 <= right1:
                # valid
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return min(right1, right2)
            else:
                if left2 > right1:
                    l = break1 + 1
                else:
                    r = break1 - 1


# @lc code=end
