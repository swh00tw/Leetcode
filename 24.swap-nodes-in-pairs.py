#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = None
        curr = head
        nxt = curr.next
        newHead = curr if nxt is None else nxt
        while curr and nxt:
            nextCurr = nxt.next
            if prev is not None:
                prev.next = nxt
            nxt.next = curr
            curr.next = nextCurr
            # update pointers
            prev = curr
            curr = nextCurr
            nxt = nextCurr.next if nextCurr is not None else None
        return newHead
        
# @lc code=end

