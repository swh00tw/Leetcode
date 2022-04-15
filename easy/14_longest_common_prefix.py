# easy
# O(n^2)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=''
        idx=0
        stop=False
        while True:
            d={}
            for s in strs:
                if idx>=len(s):
                    stop=True
                    break
                
                if s[idx] not in d:
                    d[s[idx]]=s[idx]
            if stop:
                break
                    
            if len(d)!=1:
                break
            else:
                ans+=d[strs[0][idx]]
            idx+=1
        return ans