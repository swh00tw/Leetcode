#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#

# @lc code=start
# ref: https://leetcode.com/problems/maximum-subsequence-score/editorial/
# ref: https://leetcode.com/problems/maximum-subsequence-score/solutions/3557261/python3-heap-prefixsum-beats-98/
import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(list(zip(nums1, nums2)), key=lambda x:-x[1])
        bestScore = 0
        s = 0 # sum of selected items in nums1
        h = [] # min-heap(priority queue): order by n1
        for n1, n2 in nums:
            s += n1
            heapq.heappush(h, n1)
            if len(h)==k:
                bestScore = max(bestScore, n2*s)
                s -= heapq.heappop(h)
        return bestScore
        
# @lc code=end

