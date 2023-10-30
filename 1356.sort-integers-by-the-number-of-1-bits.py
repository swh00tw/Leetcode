#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#


# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # create a function to count how many 1 bit for a number in constant time
        array = [(self.getNumOfOneBits(n), n) for n in arr]
        array.sort()
        return [x[1] for x in array]

    def getNumOfOneBits(self, num):
        binaryString = bin(num)
        one = 0
        for c in binaryString:
            if c == "1":
                one += 1
        return one


# @lc code=end
