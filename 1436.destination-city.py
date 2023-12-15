#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#


# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # create a set and put all cities inside
        # parse the paths, and keep popping out the cities paths[i][0]
        # the final city in the set is the answer
        cities = set()
        for c1, c2 in paths:
            cities.add(c1)
            cities.add(c2)
        for c1, _ in paths:
            cities.discard(c1)
        return cities.pop()


# @lc code=end
