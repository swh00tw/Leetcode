#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupSize2People = defaultdict(list)
        maxGroupSize = -1
        for i, size in enumerate(groupSizes):
            groupSize2People[size].append(i)
            maxGroupSize = max(maxGroupSize, size)
        res = []
        for size in range(1, maxGroupSize + 1):
            if len(groupSize2People[size]) == 0:
                continue
            for i in range(len(groupSize2People[size]) // size):
                start = i * size
                end = start + size
                res.append(groupSize2People[size][start:end])
        return res


# @lc code=end
