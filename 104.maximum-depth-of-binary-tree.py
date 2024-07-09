#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.traverse(root, 1)
        return self.ans

    def traverse(self, node, depth):
        if node:
            self.ans = max(self.ans, depth)
            self.traverse(node.left, depth + 1)
            self.traverse(node.right, depth + 1)


# @lc code=end
