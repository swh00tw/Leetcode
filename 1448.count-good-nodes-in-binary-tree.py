#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.visit(root, float("-inf"))
        return self.ans

    def visit(self, node, currMax):
        if node:
            if node.val >= currMax:
                self.ans += 1
            self.visit(node.left, max(node.val, currMax))
            self.visit(node.right, max(node.val, currMax))


# @lc code=end
