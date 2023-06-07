#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#

# @lc code=start
# (ai, bi) ci --> how many bit to flip
# (0, 0) 0 --> need flip 1 bit to make it 1
# (0, 1) 1 --> need flip 1 bit to make it 0
# (1, 0) 1 --> need flip 1 bit to make it 0
# (1, 1) 1 --> need flip 2 bit to make it 0
class Solution:
    def countFlipBits(self, a,b,c):
        a = int(a)
        b = int(b)
        c = int(c)
        if a==0 and b==0 and c==1:
            return 1
        if a==1 and b==1 and c==0:
            return 2
        if (a==1 or b==1) and c==0:
            return 1
        return 0
    def minFlips(self, a: int, b: int, c: int) -> int:
        aBinary = format(a, "b")
        bBinary = format(b, "b")
        cBinary = format(c, "b")
        maxL = max(len(aBinary), len(bBinary), len(cBinary))
        aBinary = "0"*(maxL-len(aBinary))+aBinary
        bBinary = "0"*(maxL-len(bBinary))+bBinary
        cBinary = "0"*(maxL-len(cBinary))+cBinary
        ans = 0
        for i in range(maxL-1, -1, -1):
            ans += self.countFlipBits(aBinary[i], bBinary[i], cBinary[i])
        return ans
# @lc code=end

