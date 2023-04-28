#
# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#

# @lc code=start
class Group:
    def __init__(self, words= []):
        self.words= words
    def canAdd(self, s):
        for x in self.words:
            diff=0
            for i in range(len(x)):
                if x[i]!=s[i]:
                    diff+=1
            if diff == 0 or diff == 2:
                return True
        return False
    def add(self, s):
        self.words.append(s)
    def __repr__(self):
        return f"{self.words}"

def mergeGroups(groups, indice, s):
    newWords=[s]
    for i in indice:
        newWords+=groups[i].words
    newGroups=[]
    for i, g in enumerate(groups):
        if i not in indice:
            newGroups.append(g)
    newGroups.append(Group(newWords))
    return newGroups

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        groups= []
        
        for s in strs:
            indice=[]
            for i, g in enumerate(groups):
                if g.canAdd(s):
                    indice.append(i)
            if len(indice)==1:
                groups[indice[0]].add(s)
            elif len(indice)==0:
                groups.append(Group([s]))
            else:
                groups=mergeGroups(groups, indice, s)
        #print(groups)
        return len(groups)
        
# @lc code=end

