#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#


# @lc code=start
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # solution 1
        # we just alter bit from each character
        # since we flip a bit from each character, we can prove that the answer must be different from each of them
        # don't believe?
        # we alter the 1st bit from 1st b_str --> guarantee different from 1st b_str
        # we alter the 2nd bit from 2nd b_str --> guarantee different from 2nd b_str
        # we alter the 3rd bit from 3rd b_str --> guarantee different from 3rd b_str
        # ...
        # we alter the nth bit from nth b_str --> guarantee different from nth b_str
        ans = []
        n = len(nums)
        for i in range(n):
            if nums[i][i] == "1":
                ans.append("0")
            else:
                ans.append("1")
        return "".join(ans)

    def solution2(self, nums):
        # 0 ~ 2^n-1
        # create a set: numberSet, contains all possible numbers can be represented by binary string of length n
        # linear traverse thru nums,
        #   convert binary str to number
        #   remove from set
        # retrieve any number in the set and transform to binary string back and return
        # TC: O(n)
        # SC: O(1)
        n = len(nums)
        numberSet = set(list(range(2**n)))
        for b_str in nums:
            numberSet.discard(self.binaryStr2Int(b_str))
        ans = numberSet.pop()
        return self.int2binaryStr(ans, n)

    def binaryStr2Int(self, string: str) -> int:
        # turn binary string to number
        bits = list(string)
        bits.reverse()
        num = 0
        for i, bit in enumerate(bits):
            if bit == "1":
                num += 2**i
        return num

    def int2binaryStr(self, num: int, length: int) -> str:
        bits = []
        n = num
        while n:
            remainder = n % 2
            n = n // 2
            bits.insert(0, str(remainder))
        # pad zero
        while len(bits) != length:
            bits.insert(0, "0")
        return "".join(bits)


# @lc code=end
