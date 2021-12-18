# O(n)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def inorder(node, res):
            if (node!=None):
                if node.left:
                    inorder(node.left,res)
                res.append(node.val)
                if node.right:
                    inorder(node.right,res)
        inorder(root,res)
        return res


# Using iterative method
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        stack = []
        curr = root
        while (curr!=None or stack):
            while curr!=None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res