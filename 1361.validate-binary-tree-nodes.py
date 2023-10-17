#
# @lc app=leetcode id=1361 lang=python3
#
# [1361] Validate Binary Tree Nodes
#


# @lc code=start
from collections import deque


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        # 1. there is a root node (have no parent)
        # 2. for each other node, has exactly one parent

        # step 1. find the root
        #   if not exactly one root --> return False
        # step 2. validate each other node has exactly one parent
        # by runnign a DFS/BFS to visit all child, in the end, all child must be visited, and no child has been visited twice(loop)

        root = None
        indices = set(range(n))
        for i in range(n):
            indices.discard(leftChild[i])
            indices.discard(rightChild[i])
        if len(indices) != 1:
            return False
        root = indices.pop()

        queue = deque([])
        queue.append(root)
        visited = [False] * n
        visited[root] = True
        while queue:
            # BFS
            idx = queue.popleft()
            # append it's children to queue and mark them to True
            # if they've been visited, return False
            if leftChild[idx] != -1:
                if visited[leftChild[idx]] is True:
                    return False
                visited[leftChild[idx]] = True
                queue.append(leftChild[idx])
            if rightChild[idx] != -1:
                if visited[rightChild[idx]] is True:
                    return False
                visited[rightChild[idx]] = True
                queue.append(rightChild[idx])

        return all(x is True for x in visited)


# @lc code=end
