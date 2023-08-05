#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # nums is always sorted
        def getRoots(nums: List[int]) -> List[Optional[TreeNode]]:
            # base case
            if len(nums) == 0:
                return [None]
            if len(nums) == 1:
                return [TreeNode(nums[0])]

            n = len(nums)
            roots = []
            for i in range(n):
                rightRoots = getRoots(nums[i + 1 :])
                leftRoots = getRoots(nums[:i])
                for rr in rightRoots:
                    for lr in leftRoots:
                        root = TreeNode(nums[i])
                        root.right = rr
                        root.left = lr
                        roots.append(root)
            return roots

        return getRoots([i + 1 for i in range(n)])


# @lc code=end
