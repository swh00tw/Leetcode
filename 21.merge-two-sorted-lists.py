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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        curr=ListNode()
        head = curr
        while p1 or p2:
            if p1 == None:
                next = ListNode(p2.val)
                p2 = p2.next
            elif p2 == None:
                next = ListNode(p1.val)
                p1 = p1.next
            else:
                if p1.val <= p2.val:
                    next = ListNode(p1.val)
                    p1 = p1.next
                else:
                    next = ListNode(p2.val)
                    p2 = p2.next
            curr.next = next
            curr = curr.next
        return head.next

        
# @lc code=end

