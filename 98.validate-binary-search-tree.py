#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursive function
        # inputs:
        # 1. node: Optional[TreeNode]
        # 2. upperBound: int
        # 3. lowerBound: int
        return self.validate(root, float("-inf"), float("inf"))

    def validate(self, node, low, high):
        if not node:
            return True
        if node.val >= high or node.val <= low:
            return False
        return self.validate(node.left, low, node.val) and self.validate(
            node.right, node.val, high
        )


# @lc code=end
