#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        return self.check(root, key)

    def check(self, node, key):
        if node:
            if node.val == key:
                # find predecessor for replacing
                predecessor = self.findPredecessor(node)
                if predecessor is None:
                    return node.left
                predecessor.left = node.left
                predecessor.right = node.right
                return predecessor
            else:
                if key > node.val:
                    node.right = self.check(node.right, key)
                else:
                    node.left = self.check(node.left, key)
                return node
        else:
            return None

    def findPredecessor(self, node):
        prev = None
        if node.right is None:
            return None
        curr = node.right
        while curr.left:
            prev = curr
            curr = curr.left
        if prev is not None:
            prev.left = curr.right
            curr.right = None
        else:
            node.right = curr.right
        return curr


# @lc code=end
