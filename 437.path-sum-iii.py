#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.pathSum(root.left, targetSum)+self.pathSum(root.right, targetSum)+self.traverse(root, targetSum)
    
    def traverse(self, node, targetSum): # find how many paths begin from "node" has sum equal to targetSum
        if not node:
            return 0
        ans = 0
        if node.val == targetSum:
            ans += 1
        # the answer also consists of left child and right child
        ans += self.traverse(node.left, targetSum-node.val)
        ans += self.traverse(node.right, targetSum-node.val)
        return ans
        

# @lc code=end

