#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # traverse each node
        # for each node, there are 4 cases
        # 1. node itself
        # 2. node + left
        # 3. node + right
        # 4. node + right + left
        self.ans = float("-inf")
        self.visit(root)
        return self.ans

    def visit(self, root):
        # base case
        if not root:
            return 0

        val = root.val
        right = self.visit(root.right)
        left = self.visit(root.left)

        # case 1, 2, 3, 4
        self.ans = max(
            [
                self.ans,
                val,
                val + left,
                val + right,
                val + left + right,
            ]
        )

        # return maxSum that exclude (val+left+right) since it cannot be used by parent
        return max([val, val + left, val + right])


# @lc code=end
