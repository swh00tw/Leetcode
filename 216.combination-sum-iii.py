#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.findAnswers(k, n, [], set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        return self.ans

    def findAnswers(self, k, n, curr, numberSet):
        if k==1:
            if n in numberSet:
                self.ans.append(curr+[n])
        else:
            for number in list(numberSet):
                if number>n:
                    continue
                nextNumberSet = set()
                for value in numberSet:
                    if value>number:
                        nextNumberSet.add(value)
                nextK = k-1
                nextN = n-number
                self.findAnswers(nextK, nextN, curr+[number], nextNumberSet)

  
        
# @lc code=end

