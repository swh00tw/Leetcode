#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start

# inspired from: https://leetcode.com/problems/best-team-with-no-conflicts/solutions/3120878/python-3-5-lines-dp-w-example-t-m-93-99/
# use DP
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        maxAge = max(ages)
        highestForEachAge = [0]*(1+maxAge) # from age zero to age maxAge
        scoreAgePairs = sorted(zip(scores, ages)) # sort bt score in ascending order
        # traverse thru pairs and keep updating table
        for score, age in scoreAgePairs:
            highestForEachAge[age] = score + max(highestForEachAge[:age+1])
        return max(highestForEachAge)


                
   
# @lc code=end

