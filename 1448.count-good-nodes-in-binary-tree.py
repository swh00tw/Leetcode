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
    def goodNodes(self, root: TreeNode) -> int:
        return self.visit(root, root.val)

    def visit(self, node: Optional[TreeNode], maximum):
        # recursive
        # the num of good nodes for a node is
        # (1 if this node is good else 0) + good nodes of left child + good nodes of right child
        if not node:
            return 0
        newMax = max(maximum, node.val)
        return (
            (1 if node.val >= maximum else 0)
            + self.visit(node.left, newMax)
            + self.visit(node.right, newMax)
        )


# @lc code=end
