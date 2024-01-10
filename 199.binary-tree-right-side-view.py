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
        # BFS
        queue = []  # nodes[]
        queue.append([root])
        ans = []
        while queue:
            nextBatch = []
            nodes = queue.pop(0)
            for n in nodes:
                if n.left:
                    nextBatch.append(n.left)
                if n.right:
                    nextBatch.append(n.right)
            ans.append(nodes[-1].val)
            if nextBatch:
                queue.append(nextBatch)
        return ans


# @lc code=end
