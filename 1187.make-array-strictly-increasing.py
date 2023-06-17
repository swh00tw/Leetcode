#
# @lc app=leetcode id=1187 lang=python3
#
# [1187] Make Array Strictly Increasing
#

# @lc code=start
# ref: https://leetcode.com/problems/make-array-strictly-increasing/solutions/3647661/python-simple-python-solution-using-dynamic-programming-sorting/
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # top-down dp, so create a cache
        # at each position, there are 0~2 choices (at most)
        # Option 1. keep the current element (if it is bigger than prev one)
        # Option 2. replace the current element by smallest element in arr2 that is larger than prev one (need binary search)
        cache = {}
        arr2 = sorted(arr2)

        def dfs(index, prevValue): # return minimum operations needed
            minOperation = float("inf")
            # base case
            if index==len(arr1):
                return 0
            if (index, prevValue) in cache: # top-down dp to avoid recalculate
                return cache[(index, prevValue)]
            
            if arr1[index]>prevValue: # option 1
                minOperation = min(minOperation, dfs(index+1, arr1[index]))
            minReplacementIdx = self.binarySearch(arr2, prevValue)
            if minReplacementIdx < len(arr2): # option 2
                minOperation = min(minOperation, 1+dfs(index+1, arr2[minReplacementIdx]))
            
            # update cache and return
            cache[(index, prevValue)] = minOperation
            return minOperation
        
        ans = dfs(0, -1)
        return ans if ans<float("inf") else -1
        

    def binarySearch(self, arr, key):
        # find the smallest number's position that is larger than key
        if key>arr[-1]:
            return len(arr)
        if key<arr[0]:
            return 0
        l, r = 0, len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid]>key:
                r = mid -1 
            else:
                l = mid +1
        return l
    


        
# @lc code=end

