#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case: length is 0 or 1
        if not head or not head.next:
            return head
        # maintain 4 pointer
        # odd head, odd tail
        # even head, even tail
        oh, ot = None, None
        eh, et = None, None
        i = 1
        curr = head
        while curr:
            next_curr = curr.next
            curr.next = None
            next_i = i + 1
            if i % 2 != 0:
                if oh is None:
                    oh = curr
                    ot = curr
                else:
                    ot.next = curr
                    ot = ot.next
            else:
                if eh is None:
                    eh = curr
                    et = curr
                else:
                    et.next = curr
                    et = et.next
            curr = next_curr
            i = next_i
        ot.next = eh
        return oh


# @lc code=end
