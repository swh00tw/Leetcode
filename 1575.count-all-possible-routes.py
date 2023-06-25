#
# @lc app=leetcode id=1575 lang=python3
#
# [1575] Count All Possible Routes
#

# @lc code=start
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # top down dp
        distance = [abs(x - locations[finish]) for x in locations]
        cache = {} # key: (start, fuel) / value: how many ways from start to finish with given fuels
        def countWays(start, fuel):
            ans = 0
            # base condition
            if start == finish:
                if fuel>0:
                    ans += 1
                elif fuel==0:
                    return 1
            if distance[start]>fuel or fuel<0:
                return 0
            # in cache
            if cache.get((start, fuel)):
                return cache[(start, fuel)]
            
            for i, x in enumerate(locations):
                if i!=start:
                    ans += countWays(i, fuel-abs(locations[start]-x))
            
            # update cache and return
            cache[(start, fuel)] = ans
            return ans
        
        res = countWays(start, fuel)
        return res % (10**9+7)
        
# @lc code=end

