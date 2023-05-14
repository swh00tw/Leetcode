#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.l = []
    def preorder(self, root: 'Node') -> List[int]:
        self.traverse(root)
        return self.l
    def traverse(self, node):
        if node is None:
            return
        self.l.append(node.val)
        for n in node.children:
            self.traverse(n)

        
# @lc code=end

