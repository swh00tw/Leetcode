#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.traverse(root, val)

    def traverse(self, node, val):
        if node:
            if node.val == val:
                return node
            left = self.traverse(node.left, val)
            right = self.traverse(node.right, val)
            if left is None:
                return right
            else:
                return left
        else:
            return None
        
# @lc code=end

