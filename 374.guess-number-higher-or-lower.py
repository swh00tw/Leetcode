#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.guessNumInRange(1, n)
        
    def guessNumInRange(self, l, r):
        mid = (l+r)//2
        res = guess(mid)
        if res == 0:
            return mid
        elif res == -1:
            return self.guessNumInRange(l, mid-1)
        else:
            return self.guessNumInRange(mid+1, r)


        # l = 1
        # r = n
        # while l<=r:
        #     guessNum = (l+r)//2
        #     res = guess(guessNum)
        #     if res==0:
        #         return guessNum
        #     elif res==1:
        #         l = guessNum+1
        #     else:
        #         r = guessNum-1
        
# @lc code=end

