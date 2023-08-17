#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#


# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ref: https://leetcode.com/problems/sliding-window-maximum/solutions/3915610/100-deque-o-n-performance-optimal/
        # maintain a deque that first element is always the largest value
        # when processing a new element,
        # if a new element is added at the end, remove element in the front which has a lower value
        # since those are useless elements
        # if the first element is out of window, remove it
        deq = deque()  # store (idx, val) pair
        res = []

        for i in range(len(nums)):
            newValue = nums[i]
            if deq and deq[0][0] < i - k + 1:
                deq.popleft()
            while deq and deq[-1][1] < newValue:
                deq.pop()
            deq.append((i, newValue))

            res.append(deq[0][1])

        return res[k - 1 :]


# @lc code=end
