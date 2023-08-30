#
# @lc app=leetcode id=2375 lang=python3
#
# [2375] Construct Smallest Number From DI String
#


# @lc code=start
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        nextNum = 1
        rev_pattern = pattern[::-1]
        consecutiveD = []
        tmp = 0
        for c in rev_pattern:
            if c == "D":
                tmp += 1
            else:
                tmp = 0
            consecutiveD.append(tmp)
        consecutiveD = consecutiveD[::-1]
        ans = ""
        for i in range(n):
            if consecutiveD[i] == 0:
                ans += str(nextNum)
                nextNum = len(ans) + 1
            else:
                tmp = nextNum + consecutiveD[i]
                ans += str(tmp)
        ans += str(nextNum)
        return ans


# @lc code=end
