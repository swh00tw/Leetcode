#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#


# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # T --> 1, F --> 0, find the longest subarray of 1s
        # F --> 1, T --> 0, find the longest subarray of 1s
        res = 0
        nums1 = []
        nums2 = []
        for c in answerKey:
            if c == "T":
                nums1.append(1)
                nums2.append(0)
            else:
                nums1.append(0)
                nums2.append(1)
        res = max(self.findLongest(nums1, k), self.findLongest(nums2, k))
        return res

    def findLongest(self, nums, chances):
        # use two pointers to represent sliding window to count 1
        # l pointer always point to the idx start counting
        n = len(nums)
        l, r = 0, -1
        zeroInWindow = 0
        best = 0
        while r < n - 1:
            r += 1
            if nums[r] == 0 and zeroInWindow < chances:
                zeroInWindow += 1
            elif nums[r] == 0 and zeroInWindow == chances:
                # update l to first zero's right
                while nums[l] != 0:
                    l += 1
                l += 1
            best = max(best, r + 1 - l)

        return best


# @lc code=end
