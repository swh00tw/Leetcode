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
        if head is None or head.next is None:
            return head
        evenHead = head.next
        curr = head
        idx = 1
        lastOdd = head
        while curr:
            if idx%2==1:
                lastOdd = curr
            if curr.next is None:
                break
            nextNode = curr.next
            curr.next = curr.next.next
            curr = nextNode
            idx += 1
        lastOdd.next = evenHead
        return head

        
        
# @lc code=end

