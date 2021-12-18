# easy
# recursive
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def inorder(node, res):
            if (node!=None):
                if node.left:
                    inorder(node.left,res)
                if node.right:
                    inorder(node.right,res)
                res.append(node.val)
        inorder(root,res)
        return res

# iterative
class Solution2(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        res=[]
        stack=[]
        stack.append(root)
        while stack:
            node = stack[-1]
            if node.left==None and node.right==None:
                node=stack.pop()
                res.append(node.val)
            if node.right:
                stack.append(node.right)
                node.right=None
            if node.left:
                stack.append(node.left)
                node.left=None
        return res