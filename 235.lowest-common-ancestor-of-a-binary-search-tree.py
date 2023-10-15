#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
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
        # the return node's value must <= q.val and >= p.val
        lower = min(p, q, key=lambda x: x.val)
        higher = max(p, q, key=lambda x: x.val)
        return self.findLCA(root, lower, higher)

    def findLCA(self, node, lower, higher):
        if node:
            # base case #1, node's val is in between lower.val and higher.val
            # lower.val < node.val < higher.val
            # base case #2, node == lower
            # base case #3, node == higher
            # The union of these cases, lower.val <= node.val <= higher.val
            if lower.val <= node.val <= higher.val:
                return node

            # if node.val > higher, search left subtree
            # else search right subtree
            if node.val > higher.val:
                return self.findLCA(node.left, lower, higher)
            else:
                return self.findLCA(node.right, lower, higher)


# @lc code=end
