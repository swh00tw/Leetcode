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
        if root is None:
            return 0
        self.traverse(root.left, 1, False)
        self.traverse(root.right, 1, True)
        return self.longest
        
    def traverse(self, node, lengthOfCurrZigZag, isRight):
        if node:
            self.longest = max(self.longest, lengthOfCurrZigZag)
            if isRight:
                self.traverse(node.right, 1, True)
                self.traverse(node.left, lengthOfCurrZigZag+1, False)
            else:
                self.traverse(node.right, lengthOfCurrZigZag+1, True)
                self.traverse(node.left, 1, False)
# @lc code=end

