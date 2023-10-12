#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.visit(root, subRoot)

    def visit(self, node, subroot):
        if node is None and subroot is None:
            return True
        if node is None or subroot is None:
            return False
        ans = False
        if node.val == subroot.val:
            ans = self.isSameTree(node, subroot)
        return ans or self.visit(node.left, subroot) or self.visit(node.right, subroot)

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


# @lc code=end
