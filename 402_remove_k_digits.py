# sol: https://leetcode.com/problems/remove-k-digits/discuss/700059/Python-Very-detail-explanation-with-examples-using-stack
class Solution(object):
    def removeKdigits(self, num, k):
        ## RC ##
		## APPROACH : STACK ##
        ## IDEA : 1234, k= 2 => when numbers are in increasing order we need to delete last digits 
        ## 4321 , k = 2 ==> when numbers are in decreasing order, we need to delete first digits
        ## so, we need to preserve increasing sequence and remove decreasing sequence ##
		## LOGIC ##
		#	1. First think in terms of stack
		#	2. push num into stack IF num it is greater than top of stack
		#	3. ELSE pop all elements less than num
		
        ## TIME COMPLEXICITY : O(N) ##
		## SPACE COMPLEXICITY : O(N) ##
        if (len(num)==k):
            return '0'
	    
        stack = []
        for n in num:
            while( stack and int(stack[-1]) > int(n) and k):
                stack.pop()
                k -= 1
            stack.append(str(n))
        
        # If no elements are removed, pop last elements, (increasing order)
        while(k):
            stack.pop()
            k -= 1

        # removing leading zero
        res = ''.join(stack)
        res = int(res)
        return str(res)
         