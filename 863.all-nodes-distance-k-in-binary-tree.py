#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def __init__(self):
        self.ans = []

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None:
            return []
        self.backtrack(root, target, k)
        return self.ans

    def backtrack(self, node, target, k):
        # return the distance between node and target
        if node is None:
            return inf
        # base
        if node == target:
            # run bfs to append children with distance k to self.ans
            res = self.bfsFindChildren(target, k)
            self.ans += res
            return 0

        leftDistance = self.backtrack(node.left, target, k) + 1
        rightDistance = self.backtrack(node.right, target, k) + 1
        if leftDistance < inf and leftDistance <= k:
            if leftDistance == k:
                self.ans.append(node.val)
            elif node.right:
                res = self.bfsFindChildren(node.right, k - leftDistance - 1)
                self.ans += res
        if rightDistance < inf and rightDistance <= k:
            if rightDistance == k:
                self.ans.append(node.val)
            elif node.left:
                res = self.bfsFindChildren(node.left, k - rightDistance - 1)
                self.ans += res
        return min(leftDistance, rightDistance)

    def bfsFindChildren(self, root, distance):
        ans = []
        q = deque([(root, 0)])
        while q:
            n, d = q.popleft()
            if d == distance:
                ans.append(n.val)
            elif d < distance:
                if n.right:
                    q.append((n.right, d + 1))
                if n.left:
                    q.append((n.left, d + 1))
        return ans


# @lc code=end
