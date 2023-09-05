#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # add an additional attribute to Node: clone
        # to point to clone node
        # initialize their random attribute to None
        if not head:
            return None
        curr = head
        prevClone = None
        while curr:
            curr.clone = Node(curr.val)
            if prevClone:
                prevClone.next = curr.clone
            prevClone = curr.clone
            curr = curr.next

        curr = head
        while curr:
            curr.clone.random = curr.random.clone if curr.random is not None else None
            curr = curr.next

        return head.clone


# @lc code=end
