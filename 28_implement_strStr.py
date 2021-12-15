# easy
# ??

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        if needle not in haystack:
            return -1
        else:
            length = len(needle)
            for i in range(len(haystack)):
                s=haystack[i:i+length]
                if (s==needle):
                    return i
            return -1