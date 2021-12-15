# Easy
# O(n)
class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        idx=0
        count=0
        last =False
        while True:
            if (idx>=length):
                break
            else:
                if (idx==length-1):
                    last=True
                if s[idx]=='I':
                    if last!=True:
                        if s[idx+1]=='V':
                            count+=4
                            idx+=2
                            continue
                    if last!=True:
                        if s[idx+1]=='X':
                            count+=9
                            idx+=2
                            continue
                    
                    count+=1
                    idx+=1
                elif s[idx]=='V':
                    count+=5
                    idx+=1
                elif s[idx]=='X':
                    if last!=True:
                        if s[idx+1]=='L':
                            count+=40
                            idx+=2
                            continue
                    if last!=True:
                        if s[idx+1]=='C':
                            count+=90
                            idx+=2
                            continue
                    
                    count+=10
                    idx+=1
                elif s[idx]=='L':
                    count+=50
                    idx+=1
                elif s[idx]=='C':
                    if last!=True:
                        if s[idx+1]=='D':
                            count+=400
                            idx+=2
                            continue
                    if last!=True:
                        if s[idx+1]=='M':
                            count+=900
                            idx+=2
                            continue
                    
                    count+=100
                    idx+=1
                elif s[idx]=='D':
                    count+=500
                    idx+=1
                elif s[idx]=='M':
                    count+=1000
                    idx+=1
        return count

# optimal
class Solution:
# @param {string} s
# @return {integer}
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]