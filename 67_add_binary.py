# easy
# O(n)

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a=='0':
            return b
        elif b=='0':
            return a
        
        length = max(len(a),len(b))
        ans = []
        a=a[::-1]
        b=b[::-1]
        carry=0
        for i in range(length):
            if i>=len(a):
                m = 0
            else:
                m= int(a[i])
            if i>=len(b):
                n=0
            else:
                n = int(b[i])
                
            digit = m+n+carry
            if digit>=2:
                digit-=2
                carry=1
            else:
                carry =0
            ans.append(str(digit))
        if carry==1:
            ans.append(str(carry))
        
        return ''.join(ans)[::-1]
        