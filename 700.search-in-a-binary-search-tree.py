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
        return self.find(root, val)

    def find(self, node, val):
        if not node:
            return None
        if node.val == val:
            return node
        left = self.find(node.left, val)
        if left:
            return left
        right = self.find(node.right, val)
        if right:
            return right
        return None


# @lc code=end
