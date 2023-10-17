#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        return self.visitNodes([root])

    def visitNodes(self, nodes) -> List[List[int]]:
        nextLevel = []
        for n in nodes:
            if n.left:
                nextLevel.append(n.left)
            if n.right:
                nextLevel.append(n.right)
        # base case
        if len(nextLevel) == 0:
            return [[n.val for n in nodes]]
        return [[n.val for n in nodes]] + self.visitNodes(nextLevel)


# @lc code=end
