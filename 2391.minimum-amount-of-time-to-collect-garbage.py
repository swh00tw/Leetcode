#
# @lc app=leetcode id=2391 lang=python3
#
# [2391] Minimum Amount of Time to Collect Garbage
#


# @lc code=start
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # special case: when no garbage in the list, the truck don't have to be used
        # we can use a recursive function to get the time needed for each type of garbage
        # get_collecting_time(start_idx, type), type: "G" | "P" | "M"
        # base time: when idx == len(garbage) - 1 or when no that type of garbage behind
        # first, preprocess using Counter
        GLASS = "G"
        METAL = "M"
        PAPER = "P"
        total_garbage = 0
        last_occurence = {}
        for i, g in enumerate(garbage):
            total_garbage += len(g)
            if GLASS in g:
                last_occurence[GLASS] = i
            if METAL in g:
                last_occurence[METAL] = i
            if PAPER in g:
                last_occurence[PAPER] = i

        travelTimePrefixSum = [0]
        for i in range(len(travel)):
            travelTimePrefixSum.append(travelTimePrefixSum[-1] + travel[i])

        ans = (
            total_garbage
            + (
                travelTimePrefixSum[last_occurence[GLASS]]
                if GLASS in last_occurence
                else 0
            )
            + (
                travelTimePrefixSum[last_occurence[METAL]]
                if METAL in last_occurence
                else 0
            )
            + (
                travelTimePrefixSum[last_occurence[PAPER]]
                if PAPER in last_occurence
                else 0
            )
        )
        return ans


# @lc code=end
