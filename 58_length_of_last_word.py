# easy
# O(n)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = s.split(' ')
        ans=''
        for word in ss:
            if word!='':
                ans = word
        return len(ans)