#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # top down dp
        cache = defaultdict(list)

        def constructFullBST(n) -> List[TreeNode]:
            if n == 0 or n == 2:
                return []
            if n == 1:
                return [TreeNode()]
            if n % 2 == 0:
                return []
            if n in cache:
                return cache[n]

            k = n - 1
            left = 1
            right = k - 1
            roots = []
            while 0 < left < k and 0 < right < k:
                leftTrees = constructFullBST(left)
                rightTrees = constructFullBST(right)
                for leftRoot in leftTrees:
                    for rightRoot in rightTrees:
                        head = TreeNode()
                        head.left = leftRoot
                        head.right = rightRoot
                        roots.append(head)
                left += 2
                right -= 2

            cache[n] = roots
            return roots

        return constructFullBST(n)


# @lc code=end
