#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, Tuple


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        h, _ = self.getRevLinkedList(head)
        return h

    def getRevLinkedList(self, node: ListNode) -> Tuple[ListNode, ListNode]:
        # given a head node, return the head and tail of the reverse linked list
        # base case: the head node doesn't have next
        # else, call getRevLinkedList and pass in next node to get the head and tail of the rev linked list
        if node.next is None:
            return node, node
        head, tail = self.getRevLinkedList(node.next)
        node.next = None
        tail.next = node
        return head, tail.next


# @lc code=end
