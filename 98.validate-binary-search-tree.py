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
        # three conditions need to be true
        # root.val is within upperbound and lowerbound
        # left tree is valid
        # right tree is valid
        return self.isValidRoot(root, float("-inf"), float("inf"))

    def isValidRoot(self, root, lowerbound, upperbound):
        if root is None:
            return True
        return (
            self.isValidRoot(root.left, lowerbound, root.val)
            and self.isValidRoot(root.right, root.val, upperbound)
            and (lowerbound < root.val < upperbound)
        )


# @lc code=end
