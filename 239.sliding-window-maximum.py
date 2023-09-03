#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#


# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a deque to store (val, idx) in the window
        # the queue is in descending order, maintained by the following rule:
        # When a new num is being added,
        # keep elminate num from the end if the top val of queue is lower than new num
        # since the previous lower value is useless,
        # it is impossible to be max and it will disappear earlier than the new num
        # so it's no reason for it to be store in the queue
        # When sliding window move,
        # pop one from the start of the queue if needed (check idx)
        # by doing so, the maximum value of window is at the front of the queue
        q = deque()
        for i in range(k):
            while q and q[-1][0] <= nums[i]:
                q.pop()
            q.append((nums[i], i))

        ans = []
        ans.append(q[0][0])
        for right in range(k, len(nums)):
            left = right + 1 - k
            if q[0][1] < left:
                q.popleft()
            newNum = nums[right]
            while q and q[-1][0] <= newNum:
                q.pop()
            q.append((newNum, right))
            ans.append(q[0][0])
        return ans


# @lc code=end
