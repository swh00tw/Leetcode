#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#


# @lc code=start
from collections import deque


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
        # if encounter 1, increment count
        # if encounter 0 but zeroIdxQueue's length < chances, increment count and push a index
        # else, pop a zeroIdx and push a new idx
        best = 0
        startIdx = 0  # keep track of start counting idx
        zeroIdxQueue = deque([])  # max length = chances
        for i, n in enumerate(nums):
            if n == 0 and len(zeroIdxQueue) < chances:
                zeroIdxQueue.append(i)
            elif n == 0 and len(zeroIdxQueue) == chances:
                idx = zeroIdxQueue.popleft()
                zeroIdxQueue.append(i)
                # update startIdx
                idx = idx + 1
                while True:
                    if nums[idx] == 1:
                        break
                    if idx == zeroIdxQueue[0]:
                        break
                    idx += 1
                startIdx = idx
            best = max(best, i + 1 - startIdx)
        return best


# @lc code=end
