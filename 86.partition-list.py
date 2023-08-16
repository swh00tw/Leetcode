#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lowerHead = ListNode()
        lowerCurr = lowerHead
        higherHead = ListNode()
        higherCurr = higherHead
        curr = head
        while curr:
            if curr.val >= x:
                higherCurr.next = ListNode(curr.val)
                higherCurr = higherCurr.next
            else:
                lowerCurr.next = ListNode(curr.val)
                lowerCurr = lowerCurr.next
            curr = curr.next
        lowerCurr.next = higherHead.next
        return lowerHead.next


# @lc code=end
