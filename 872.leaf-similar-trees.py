#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = self.getLeaf(root1)
        leaf2 = self.getLeaf(root2)
        return leaf1==leaf2

    def getLeaf(self, root):
        leaf = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not (node.left or node.right): # isLeaf
                leaf.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return leaf
        
# @lc code=end

