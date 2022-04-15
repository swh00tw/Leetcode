# easy
# O(lgn)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        def binary_search(arr,target, p,r):
            if p==r:
                if arr[p]==target:
                    return p
                elif target<arr[p]:
                    return p
                else:
                    return p+1
            elif r>p:
                q = (p+r)//2
                if target>arr[q]:
                    return binary_search(arr,target,q+1,r)
                else:
                    return binary_search(arr,target,p,q)
                
        return binary_search(nums,target,0,len(nums)-1)