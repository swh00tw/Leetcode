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
    def __init__(self):
        self.count = 0
        
    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root, -inf)
        return self.count

    def traverse(self, node, currentLargest):
        if node:
            # is it good?
            nextLargest = currentLargest
            if node.val >= currentLargest:
                self.count += 1
                nextLargest = node.val
            self.traverse(node.left, nextLargest)
            self.traverse(node.right, nextLargest)
# @lc code=end

