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
        if root is None:
            return []
        q = [(root, 0)] # (node, depth)
        maxDepth = 0
        rsv = {}
        while q:
            node, depth = q.pop(0)
            maxDepth = max(maxDepth, depth)
            rsv[depth] = node.val
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        return [rsv[i] for i in range(maxDepth+1)]

# @lc code=end

