# easy

# recursive
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def inorder(node, res):
            if (node!=None):
                res.append(node.val)
                if node.left:
                    inorder(node.left,res)
                if node.right:
                    inorder(node.right,res)
        inorder(root,res)
        return res
    
# iterative
class Solution2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res=[]
        stack=[]
        stack.append(root)
        while stack:
            node = stack.pop()
            if node==None:
                break
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res