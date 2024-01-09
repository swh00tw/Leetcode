#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flattenHelper(root)

    def flattenHelper(self, root: TreeNode) -> TreeNode:
        # flatten and return the last node
        if not root.left and not root.right:
            return root
        if not root.left:
            return self.flattenHelper(root.right)
        if not root.right:
            leftTail = self.flattenHelper(root.left)
            root.right = root.left
            root.left = None
            return leftTail
        leftTail = self.flattenHelper(root.left)
        rightTail = self.flattenHelper(root.right)
        leftTail.right = root.right
        root.right = root.left
        root.left = None
        return rightTail


# @lc code=end
