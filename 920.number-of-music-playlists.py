#
# @lc app=leetcode id=920 lang=python3
#
# [920] Number of Music Playlists
#

# @lc code=start
import math


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # top down dp
        cache = {}  # key = (n, goal)

        def getAns(
            uniqueNums, length
        ):  # n: number of unique numbers, goal: playlist's length
            # base case
            if uniqueNums == 0 and length == 0:
                return 1
            # if goal length is 0 and the unique number we must use is not 0
            # or
            # if the unique numbers we must use is 0 and the goal length isn't 0
            if uniqueNums == 0 or length == 0:
                return 0
            # in cache
            if (uniqueNums, length) in cache:
                return cache[(uniqueNums, length)]

            ans = 0
            # the curr position is gained from choosing a number that never appear before
            # therefore, it's from "using n-1 unique numbers to form a playlist which length is goal-1"
            # and the current choices is n-(uniqueNums-1)
            ans += getAns(uniqueNums - 1, length - 1) * (n - uniqueNums + 1)
            # the curr position is gained from using the number that appears before
            # therefore, it's from "using n unique numbers to form a playlist which length is length-1"
            # and the current choices is (uniqueNums-k) due to the constraint (there are k nums in the set we can't use)
            if uniqueNums - k > 0:
                ans += getAns(uniqueNums, length - 1) * (uniqueNums - k)

            # save and return
            ans %= 10**9 + 7
            cache[(uniqueNums, length)] = ans
            return ans

        return getAns(n, goal)


# @lc code=end
