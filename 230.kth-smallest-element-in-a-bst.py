#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        preorder = self.getPreorder(root)
        return preorder[k - 1]

    def getPreorder(self, root):
        if root is None:
            return []
        return self.getPreorder(root.left) + [root.val] + self.getPreorder(root.right)


# @lc code=end
