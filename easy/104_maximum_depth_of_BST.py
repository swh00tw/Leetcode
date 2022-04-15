# O(n)
# recommend sol: https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/359949/Python-recursive-and-iterative-solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        max_depth = [1]
        root.depth = 1
        def preorder(node, max_depth):
            #print('val: ',node.val)
            #print("depth: ",node.depth)
            if node.depth>max_depth[0]:
                max_depth[0] = node.depth
            
            
            if node.left:
                node.left.depth = node.depth+1
                preorder(node.left, max_depth)
                
            
            if node.right:
                node.right.depth=node.depth+1
                preorder(node.right, max_depth)
        preorder(root, max_depth)
        return max_depth[0]