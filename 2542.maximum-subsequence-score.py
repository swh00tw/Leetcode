#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#

# @lc code=start
# ref: https://leetcode.com/problems/maximum-subsequence-score/editorial/
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = -1
        pairs = sorted(list(zip(nums1, nums2)), key=lambda x: -x[1])
        topNumbers = [
            p[0] for p in pairs[: k - 1]
        ]  # keep track of top k-1 numbers currently discovered
        heapq.heapify(topNumbers)
        sumOfHeap = sum(topNumbers)

        for pair in pairs[k - 1 :]:
            multiplier = pair[1]
            s = pair[0] + sumOfHeap
            res = max(res, s * multiplier)
            # update topNumbers
            heapq.heappush(topNumbers, pair[0])
            deleteNum = heapq.heappop(topNumbers)
            sumOfHeap = sumOfHeap + pair[0] - deleteNum
        return res


# @lc code=end
