#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create a stack s --> the day element in stack means they are waiting for a warmer day
        # parse t in temperatures, 
        # when t <= s.top[0], push (t, index) onto stack
        # else, pop the top until t<=s.top[0]
        # each time pop the top item from stack, record the index difference(number of days to wait)
        s = []
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            if len(s)!=0 and t>s[-1][0]:
                while len(s)>0 and t>s[-1][0]:
                    day = s.pop()
                    indexDiff = i-day[1]
                    res[day[1]] = indexDiff
            s.append([t, i])
        return res
        
# @lc code=end

