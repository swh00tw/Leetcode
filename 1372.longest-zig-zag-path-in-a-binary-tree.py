#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.longest = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.visit(root.left, False, 1)
        self.visit(root.right, True, 1)
        return self.longest

    def visit(self, node, isRightChild, l):
        if not node:
            return
        self.longest = max(l, self.longest)
        if isRightChild:
            self.visit(node.right, True, 1)
            self.visit(node.left, False, l + 1)
        else:
            self.visit(node.left, False, 1)
            self.visit(node.right, True, l + 1)


# @lc code=end
