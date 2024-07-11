#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0
        ans = (1, root.val)  # level, bestSum
        queue = [root]
        level = 1
        while queue:
            _nextQ = []
            _sum = 0
            for node in queue:
                _sum += node.val
                if node.left:
                    _nextQ.append(node.left)
                if node.right:
                    _nextQ.append(node.right)
            if _sum > ans[1]:
                ans = (level, _sum)
            queue = _nextQ
            level += 1
        return ans[0]


# @lc code=end
