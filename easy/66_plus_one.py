# easy
# O(n)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        rev_digits = digits.reverse()
        num=0
        for i in range(len(digits)):
            unit = 10**(i)
            num += unit*digits[i]
        num+=1
        ans = []
        length = len(str(num))
        while (length!=0):
            digit = num//10**(length-1)
            ans.append(digit)
            num -= digit*10**(length-1)
            length-=1
        return ans