#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # pathSum(root.left, targetSum-root.val) + pathSum(root.right, targetSum-root.val)
        # + pathSum(root.left, targetSum) + pathSum(root.right, targetSum)
        # + 1 if root.val == targetSum
        self.sum = targetSum
        if not root:
            return 0
        return (
            self.countPathSum(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )

    def countPathSum(self, node: Optional[TreeNode], targetSum):
        if not node:
            return 0
        ans = 0
        if node.val == targetSum:
            ans += 1
        return (
            ans
            + self.countPathSum(node.left, targetSum - node.val)
            + self.countPathSum(node.right, targetSum - node.val)
        )


# @lc code=end
