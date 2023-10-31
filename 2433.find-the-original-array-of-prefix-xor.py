#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#


# @lc code=start
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # base: arr[0] = pref[0]
        # pref[i-1]^arr[i] = pref[i]
        # keep using this relationship, we can get the arr[i] and whole array
        # bitwise xor properties:
        # pref[i-1]^pref[i-1]^arr[i] = pref[i-1]^pref[i]
        # arr[i] = pref[i-1]^pref[i]

        n = len(pref)
        arr = [pref[0]] * n
        for i in range(1, n):
            arr[i] = pref[i - 1] ^ pref[i]
        return arr


# @lc code=end
