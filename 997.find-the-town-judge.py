#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # create an array to store the relationship of being trusted
        # arr[i] = # of people trust him/her
        numOfTrust = [0]*n
        # create a hasmap to track the people who trust someone
        # key = the person who trust someone
        givenTrust = {}
        # parse the given array
        for relationship in trust:
            givenTrust[relationship[0]-1] = True
            trustedIndex = relationship[1]-1
            numOfTrust[trustedIndex] += 1
        # the result must be only one person has n-1 trusted,
        # and the rest of people has 0 trusted
        peopleHasNMinusOneTrust = 0
        judgeIndex = -1
        for i in range(n):
            if numOfTrust[i] == n-1:
                peopleHasNMinusOneTrust += 1
                judgeIndex = i
        
        if peopleHasNMinusOneTrust == 1 and givenTrust.get(judgeIndex) == None:
            return judgeIndex+1
        else:
            return -1
            
        
# @lc code=end

