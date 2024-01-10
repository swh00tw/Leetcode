#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        return self.visitLevel([root])

    def visitLevel(self, nodes):
        if not nodes:
            return []
        nextLevel = []
        acc = 0
        for n in nodes:
            if n.left:
                nextLevel.append(n.left)
            if n.right:
                nextLevel.append(n.right)
            acc += n.val
        return [acc / len(nodes)] + self.visitLevel(nextLevel)


# @lc code=end
