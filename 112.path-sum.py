#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        subtreeTarget = targetSum - root.val
        if root.left == None and root.right == None:
            return subtreeTarget == 0
        elif root.left == None and root.right != None:
            return self.hasPathSum(root.right, subtreeTarget)
        elif root.right == None and root.left != None:
            return self.hasPathSum(root.left, subtreeTarget)
        else:
            return self.hasPathSum(root.left, subtreeTarget) or self.hasPathSum(root.right, subtreeTarget)
        
# @lc code=end

