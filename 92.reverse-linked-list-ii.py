#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        nodes = [ListNode(0)]
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = None
            nodes.append(curr)
            curr = nextNode

        newNodes = nodes[:left] + nodes[left : right + 1][::-1] + nodes[right + 1 :]
        newNodes.pop(0)
        nodes = newNodes
        for i in range(1, len(nodes)):
            nodes[i - 1].next = nodes[i]
        return nodes[0]


# @lc code=end
