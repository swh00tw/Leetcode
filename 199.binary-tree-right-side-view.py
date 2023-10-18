#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.visitNextLevel([root])

    def visitNextLevel(self, nodes):
        nextLevel = []
        # base case, no next level
        for n in nodes:
            if n.left:
                nextLevel.append(n.left)
            if n.right:
                nextLevel.append(n.right)
        if not nextLevel:
            return [nodes[-1].val]
        return [nodes[-1].val] + self.visitNextLevel(nextLevel)


# @lc code=end
