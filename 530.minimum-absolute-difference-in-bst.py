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
    def __init__(self):
        self.prevValue = -1
        self.ans = inf
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.ans

    def traverse(self, node):
        # in-order traverse
        if node:
            self.traverse(node.left)
            if self.prevValue != -1:
                self.ans = min(self.ans, abs(node.val-self.prevValue))
            self.prevValue = node.val
            self.traverse(node.right)
            
        
# @lc code=end

