# Easy
# O(n)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            elif i in ')]}':
                if  stack==[]:
                    return False
                else:
                    j=stack.pop()
                    if i==')' and j!='(':
                        return False
                    elif i==']' and j!='[':
                        return False
                    elif i=='}' and j!='{':
                        return False
                    else:
                        continue
        if stack==[]:
            return True
        else:
            return False