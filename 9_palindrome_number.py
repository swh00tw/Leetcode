# Easy
# O(n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        print(x_str)
        length = len(x_str)
        
        for i in range(length):
            a=i
            b=length-1-i
            if (x_str[a]!=x_str[b]):
                return False
        return True