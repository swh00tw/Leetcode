#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        findOne = False
        findCycle = False
        nums = {}
        curr = n
        while findOne == False and findCycle == False:
            next = self.computeNextNum(curr)
            if (next==1):
                findOne = True
                break
            elif next in nums and nums[next]>=2:
                findCycle = True
                break
            else:
                nums[next] = nums.get(next, 0)+1
                curr = next

        return findOne and not findCycle

    def computeNextNum(self, n: int):
        nums = [int(s) for s in list(str(n))]
        sum = 0
        for m in nums:
            sum += m**2
        return sum
        
# @lc code=end

