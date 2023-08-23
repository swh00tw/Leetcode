#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#


# @lc code=start
# sol: https://leetcode.com/problems/reorganize-string/solutions/3948110/easy-solution-python3-c-c-java-python-with-image/
from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        chars = Counter(s)
        ans = ""
        prev = None  # the heap item we should push back in next iteration
        maxHeap = [[-cnt, char] for char, cnt in chars.items()]
        heapq.heapify(maxHeap)

        # defer the heapq.push to the end of next iteration
        # to make sure two consecutive heappop won't get the same char
        while True:
            # finish the building process
            if not prev and not maxHeap:
                return ans
            # run out of choices, impossible to build
            if prev and not maxHeap:
                return ""

            count, char = heapq.heappop(maxHeap)
            ans += char
            charLeft = -(count + 1)

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            # if the char has more than zero in heap, store in prev and pushback in next iter
            if charLeft > 0:
                prev = [-charLeft, char]


# @lc code=end
