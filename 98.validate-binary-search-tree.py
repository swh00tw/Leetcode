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
    def __init__(self):
        self.nodes = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        n = len(self.nodes)
        i = 0
        while 0<=i<=n-2:
            if self.nodes[i]>=self.nodes[i+1]:
                return False
            i+=1
        return True        

    def inorder(self, node):
        if node:
            if node.left:
                self.inorder(node.left)
            self.nodes.append(node.val)
            if node.right:
                self.inorder(node.right)

## another solution
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
#         def helper(node, low, high):
#             if not node:
#                 return True
#             if not (low < node.val < high):
#                 return False
#             return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
#         return helper(root, -inf, inf)

# @lc code=end

