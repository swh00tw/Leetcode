#
# @lc app=leetcode id=1802 lang=python3
#
# [1802] Maximum Value at a Given Index in a Bounded Array
#

# @lc code=start
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # initialize an array (length is n, values are zero)
        # keep increment as long as sum not exceeding maxSum
        # if possible, increment nums[index]
        # we have also increment its neighbor, and neighbor's neighbor ...
        # the answer must look like a ladder
        # if n = 6, index = 1,  maxSum = 10,
        # ans: [2,3,2,1,1,1]
        # since we know the value at nums[index] would be bounded in [0, maxSum]
        # and the sums at left part and right part can be calculated in constant time
        # use Binary Search to guess the answer

        # first, assign 1 to each index, nums[index] has base value 
        maxSum -= n
        baseValue = 1
        # binary search(find rightmost answer)
        l, r = 0, maxSum
        while l<=r:
            guessAnswer = (l+r)//2
            blocksRequired = self.calculateBlocksNeeded(guessAnswer, index, n)
            if blocksRequired == maxSum:
                return guessAnswer+baseValue
            elif blocksRequired<maxSum:
                l = guessAnswer+1
            else:
                r = guessAnswer-1
        answer = (l-1)+baseValue
        return answer

    def calculateBlocksNeeded(self, guess, index, n):
        require = guess
        if index!=0:
            leftUpperBound = (index-1, guess-1) #(index, value)
            leftLowerBound = (index-guess+1, 1) if index-guess+1>=0 else (0,guess-index)
            require += ((leftUpperBound[1]+leftLowerBound[1])*(leftUpperBound[0]-leftLowerBound[0]+1))//2
        if index!=n-1:
            rightLowerBound = (index+1, guess-1)
            rightUpperBound = (index+guess-1, 1) if index+guess-1<n else (n-1, guess-(n-1-index))
            require += ((rightLowerBound[1]+rightUpperBound[1])*(rightUpperBound[0]-rightLowerBound[0]+1))//2
        return require
# @lc code=end

