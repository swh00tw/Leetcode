# easy
# O(n)
# DP is faster than using recursive, because recursive will recompute the same subproblem over and over again. 

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            res=[1,2]
            for i in range(2,n):
                res.append(res[i-1]+res[i-2])
            return res[n-1]