#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        numberOfDigits = len(str(num))
        if (numberOfDigits==1):
            return num
        else:
            nums = list(str(num))
            # print(nums)
            sum = 0
            for n in nums:
                sum += int(n)
            return self.addDigits(sum)
# @lc code=end

