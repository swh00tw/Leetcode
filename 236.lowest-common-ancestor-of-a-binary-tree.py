#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # cannot find LCA
        if not root:
            return None
        # some possibilities the answer is root itself
        if root == p or root == q:
            return root
        # the answer is from left child?
        left = self.lowestCommonAncestor(root.left, p, q)
        # the answer is from right child?
        right = self.lowestCommonAncestor(root.right, p, q)
        # if it's not from left child, the answer must at right child
        if left == None:
            return right
        # it's not from right child, the answer must at left child
        if right == None:
            return left
        # it's both left and right have LCA answer,
        # it means p and q locate at two different sides of node, the answer is root
        else:
            return root


# @lc code=end
