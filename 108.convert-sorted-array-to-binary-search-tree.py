#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if (len(nums)==0):
            return None
        length = len(nums)
        middleIndex = length//2
        leftSubtree = nums[:middleIndex]
        rightSubtree = nums[middleIndex+1:]
        leftRoot = self.sortedArrayToBST(leftSubtree)
        rightRoot = self.sortedArrayToBST(rightSubtree)
        
        root = TreeNode(val=nums[middleIndex], left=leftRoot, right=rightRoot)
        return root
        
# @lc code=end

