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
    def __init__(self):
        self.d = {} # map level to vals
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root, 0)
        res = []
        for v in self.d.values():
            res.append(v)
        return res

    def traverse(self, node, level):
        if node is None:
            return
        
        if self.d.get(level):
            self.d[level].append(node.val)
        else:
            self.d[level] = [node.val]
        
        self.traverse(node.left, level+1)
        self.traverse(node.right, level+1)
        
# @lc code=end

