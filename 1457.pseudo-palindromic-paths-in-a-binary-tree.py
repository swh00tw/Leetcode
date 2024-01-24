#
# @lc app=leetcode id=1457 lang=python3
#
# [1457] Pseudo-Palindromic Paths in a Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        # visit until reach leaf
        # pass the current state as special set
        # the number in the set is the number that shows up odd times
        init_set = set()
        self.ans = 0
        self.visit(root, init_set)
        return self.ans

    def visit(self, node, n_set):
        # clone the set
        num_set = copy.copy(n_set)
        if node.val in num_set:
            num_set.discard(node.val)
        else:
            num_set.add(node.val)

        if node.left is None and node.right is None:
            if len(num_set) <= 1:
                self.ans += 1
            return

        if node.left:
            self.visit(node.left, num_set)
        if node.right:
            self.visit(node.right, num_set)


# @lc code=end
