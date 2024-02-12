#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans = float("inf")
        self.traverse(root, float("inf"), float("-inf"))
        return self.ans

    def traverse(self, node, upperbound, lowerbound):
        if node:
            self.ans = min(self.ans, upperbound - node.val, node.val - lowerbound)
            self.traverse(node.left, node.val, lowerbound)
            self.traverse(node.right, upperbound, node.val)


# @lc code=end
