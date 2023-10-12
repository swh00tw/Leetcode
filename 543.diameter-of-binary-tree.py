#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.visit(root)
        return self.ans

    def visit(self, node):
        # diameter comes from two cases
        # it pass through root
        # not from root

        # update self.ans and
        # return max depth

        if not node:
            return 0
        else:
            leftDepth = self.visit(node.left)
            rightDepth = self.visit(node.right)
            maxDepth = 1 + max(leftDepth, rightDepth)
            self.ans = max(self.ans, abs(leftDepth + rightDepth))
            return maxDepth


# @lc code=end
