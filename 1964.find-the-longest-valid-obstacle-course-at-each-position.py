#
# @lc app=leetcode id=1964 lang=python3
#
# [1964] Find the Longest Valid Obstacle Course at Each Position
#

# @lc code=start
import bisect
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # dynamic programming
        # maintain an array that record the longest increasing obstacles so far
        # when parse a new number, use binary search to find the idx it should be inserted
        # if it's greater or equal (so we use bisect_right) than all number in the array, append to the end
        # else, replace the number have the same index as the given idx
                       
        longestValidNums = []
        ans = []

        for obstacle in obstacles:
            idx = bisect.bisect_right(longestValidNums, obstacle)
            if idx == len(longestValidNums):
                longestValidNums.append(obstacle)
            else:
                longestValidNums[idx]=obstacle # consider the case [1, 100, 2, 3, 4] will help you understand why we have this step
            ans.append(idx+1)
        return ans
            
        
# @lc code=end

