#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None
        # run BFS on original graph
        # for each node, add an additional property: a pointer point to its cloned node
        # while BFS, link the node to its neighbors
        # return the node's clone
        queue = []
        node.clone = Node(node.val, None)
        queue.append(node)
        seen = set()
        seen.add(node.val)
        while queue:
            n = queue.pop(0)
            for neighbor in n.neighbors:
                if neighbor.val not in seen:
                    seen.add(neighbor.val)
                    queue.append(neighbor)
                # build n.clone's neighbors
                if not hasattr(neighbor, "clone"):
                    neighbor.clone = Node(neighbor.val)
                n.clone.neighbors.append(neighbor.clone)
        return node.clone


# @lc code=end
