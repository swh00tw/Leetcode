#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = ListNode(0)
        prev = head
        while p1 and p2:
            node = p1 if p1.val < p2.val else p2
            if p1.val < p2.val:
                p1 = p1.next
            else:
                p2 = p2.next
            prev.next = node
            prev = prev.next
        if p1 is None:
            prev.next = p2
        else:
            prev.next = p1
        return head.next


# @lc code=end
