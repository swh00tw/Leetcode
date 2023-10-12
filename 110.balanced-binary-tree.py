#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if left and right's height diff by more than one, return false
        self.ans = True
        self.visit(root)
        return self.ans

    def visit(self, node):
        if not node:
            return 0
        leftHeight = self.visit(node.left)
        rightHeight = self.visit(node.right)
        if abs(leftHeight - rightHeight) > 1:
            self.ans = False
        return 1 + max(leftHeight, rightHeight)


# @lc code=end
