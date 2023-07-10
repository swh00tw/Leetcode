#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root, 1)

    def dfs(self, node: TreeNode, depth):
        if not node.left and not node.right:
            return depth
        leftMinDepth = self.dfs(node.left, depth + 1) if node.left else inf
        rightMinDepth = self.dfs(node.right, depth + 1) if node.right else inf
        return min(leftMinDepth, rightMinDepth)


# @lc code=end
