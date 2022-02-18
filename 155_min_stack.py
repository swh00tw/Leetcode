# easy

class MinStack(object):

    def __init__(self):
        self.min=None
        self.stack=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.min==None:
            self.min=val
        self.stack.append(val)
        if val<self.min:
            self.min=val
        

    def pop(self):
        """
        :rtype: None
        """
        val=self.stack.pop()
        
        if val==self.min:
            new_min=None
            for i in self.stack:
                if new_min==None or i<new_min:
                    new_min=i
            self.min = new_min
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()