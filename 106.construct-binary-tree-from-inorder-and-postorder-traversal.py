#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder: left, mid, right
        # postorder: left, right, mid
        # rev_postorder: mid, right, left
        # rev_inorder: right, mid, left
        # rev_postorder: [3, 20, 7, 15, 9]
        # rev_inorder: [7, 20, 15, 3, 9]
        if not inorder:
            return None
        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[idx + 1 :], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        return root


# @lc code=end
