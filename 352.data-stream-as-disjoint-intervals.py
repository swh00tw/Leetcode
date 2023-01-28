#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#

# @lc code=start
class NumUnion:
    def __init__(self, firstNum):
        self.nums = [firstNum]
        self.min = firstNum
        self.max = firstNum
    def isAddable(self, newValue):
        if newValue == self.max+1:
            return True
        return False
    def updateMax(self, val):
        self.max = val

class SummaryRanges:

    def __init__(self):
        self.nums = [] # keep sorted

    def binarySearchFindInsertIndex(self, value):
        # return [hasFind, position]
        size = len(self.nums)
        left = 0
        right = size-1
        while left<=right:
            mid = (left+right)//2
            if self.nums[mid]>value:
                right = mid-1
            elif self.nums[mid]<value:
                left = mid+1
            else:
                return [True, mid]
        return [False, left]

    def addNum(self, value: int) -> None:
        hasFind, insertPosition = self.binarySearchFindInsertIndex(value)
        if (hasFind):
            return
        self.nums = self.nums[:insertPosition]+[value]+self.nums[insertPosition:]

    def getIntervals(self) -> List[List[int]]:
        # linear time find union
        if len(self.nums) == 0:
            return []
        unions=[]
        union = NumUnion(self.nums[0])
        for i in range(1,len(self.nums)):
            newValue = self.nums[i]
            if union.isAddable(newValue):
                union.updateMax(newValue)
            else:
                unions.append(union)
                union = NumUnion(newValue)
        unions.append(union)
        return [[u.min, u.max] for u in unions]
        
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
# @lc code=end

