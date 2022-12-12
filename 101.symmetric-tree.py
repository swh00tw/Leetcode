#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isTwoTreeSymmetric(root.left, root.right)
        
    def isTwoTreeSymmetric(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        else:
            return root1.val == root2.val and self.isTwoTreeSymmetric(root1.left, root2.right) and self.isTwoTreeSymmetric(root1.right, root2.left)
# @lc code=end

