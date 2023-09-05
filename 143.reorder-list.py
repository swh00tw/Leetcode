#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        # for each node, add an attribute: prev
        curr = head
        prev = None
        while curr:
            curr.prev = prev
            prev = curr
            curr = curr.next

        tail = prev
        curr = head
        while curr:
            if curr.next == tail or curr == tail:
                break
            # detach the tail node from its prev node side, and update tail's position
            tail.prev.next = None
            node = tail
            tail = tail.prev
            # update links
            node.next = curr.next
            curr.next = node
            # update curr's position
            curr = node.next


# @lc code=end
