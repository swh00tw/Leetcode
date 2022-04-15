# easy
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        num = columnNumber
        num2char='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = []
        while num > 0:
            result.append(num2char[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)