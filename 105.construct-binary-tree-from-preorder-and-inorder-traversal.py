#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # recursive
        # start from first number in preorder
        # it will split the inorder into two array
        # pass two set of inorder, preorder to same function that return root
        # base case
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = preorder[0]
        left_in = []
        left = set()
        right_in = []
        right = set()
        curr = "Left"
        for n in inorder:
            if n == root:
                curr = "Right"
                continue
            if curr == "Left":
                left.add(n)
                left_in.append(n)
            else:
                right.add(n)
                right_in.append(n)
        left_pre = []
        right_pre = []
        for n in preorder:
            if n == root:
                continue
            if n in left:
                left_pre.append(n)
            if n in right:
                right_pre.append(n)
        rootNode = TreeNode(root)
        leftChild = self.buildTree(left_pre, left_in)
        rightChild = self.buildTree(right_pre, right_in)
        rootNode.left = leftChild
        rootNode.right = rightChild
        return rootNode


# @lc code=end
