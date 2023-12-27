#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
from collections import deque


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        queue = deque(list(s))
        for c in t:
            if c == queue[0]:
                queue.popleft()
                if len(queue) == 0:
                    return True


# @lc code=end
