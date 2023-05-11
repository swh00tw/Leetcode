#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sortedStr = ''.join(sorted(s))
            if d.get(sortedStr):
                d[sortedStr].append(s)
            else:
                d[sortedStr] = [s]
        groups = []
        for k in d:
            groups.append(d[k])
        return groups


        
# @lc code=end

