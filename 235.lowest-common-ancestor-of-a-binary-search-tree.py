#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # keep travesing nodes
        # when we traverse a node, if both p and q in right(or left) subtree, traverse right(or left)
        # if this happened: p.val <= node.val <= q.val (or p, q switch position), the node is the lca
        small = min(q.val, p.val)
        large = max(p.val, q.val)
        return self.traverse(root, small, large)

    def traverse(self, node, small, large):
        if node:
            if small <= node.val <= large:
                return node
            elif node.val < small:
                return self.traverse(node.right, small, large)
            else:
                return self.traverse(node.left, small, large)
        
# my first sol(the time complexity is optimal, but a little bit redundant, not elegant)
# def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         path1 = self.findNode(root, 0, p.val)
#         path2 = self.findNode(root, 0, q.val)
#         idxSet = set()
#         indexToNode = {}
#         lca = (root, 0)
#         for n, i in path1:
#             idxSet.add(i)
#             indexToNode[i]=n
#         for n, i in path2:
#             if i in idxSet:
#                 if i>lca[1]:
#                     lca = (n, i)
#         return lca[0]
#     def findNode(self, node, index, target): 
#         # return (node, index)[]
#         # node index is n
#         # left: 2n+1
#         # right: 2n+2
#         # root: 0
#         if not node:
#             return []
#         if node.val == target:
#             return [(node, index)]
#         elif target < node.val:
#             return [(node, index)]+self.findNode(node.left, 2*index+1, target)
#         else:
#             return [(node, index)]+self.findNode(node.right, 2*index+2, target)

# @lc code=end

