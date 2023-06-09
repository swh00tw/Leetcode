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
        q = [(root, 1)]
        depthToVal = {}
        maxDepth = 1
        while q:
            node, depth = q.pop(0)
            maxDepth = max(maxDepth, depth)
            depthToVal[depth] = depthToVal.get(depth, 0) + node.val
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
                
        ans = (root.val, 1) # val, depth
        for depth in range(1, maxDepth+1):
            if depthToVal[depth]>ans[0]:
                ans = (depthToVal[depth], depth)
        return ans[1]
        
# @lc code=end

