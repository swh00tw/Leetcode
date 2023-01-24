#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Person:
    def __init__(self, id):
        self.id=id
        self.number = id+1
        self.givenTrust=0
        self.beingTrusted=0

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [Person(i) for i in range(n)]
        # parse the array
        for i in range(len(trust)):
            people[trust[i][0]-1].givenTrust+=1
            people[trust[i][1]-1].beingTrusted+=1
        # find the judge
        for p in people:
            if p.givenTrust==0 and p.beingTrusted==n-1:
                return p.number
        return -1
    


            
        
# @lc code=end

