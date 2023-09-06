#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count the length
        # the target node's idx: length-n
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        curr = head
        prev = None
        targetIdx = length - n
        currIdx = 0
        if targetIdx == 0:
            return head.next
        while currIdx != targetIdx:
            prev = curr
            curr = curr.next
            currIdx += 1

        prev.next = curr.next
        return head


# @lc code=end
