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
        leave1 = self.getLeave(root1)
        leave2 = self.getLeave(root2)
        return leave1 == leave2

    def getLeave(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.getLeave(root.left) + self.getLeave(root.right)


# @lc code=end
