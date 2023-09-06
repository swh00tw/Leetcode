#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        addOne = False
        prevRes = ListNode()
        curr = prevRes
        while p1 or p2:
            val1 = p1.val if p1 is not None else 0
            val2 = p2.val if p2 is not None else 0
            val = val1 + val2
            if addOne is True:
                addOne = False
                val += 1
            addOne = val >= 10
            val %= 10
            newNode = ListNode(val)
            curr.next = newNode
            curr = curr.next
            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next
        if addOne is True:
            curr.next = ListNode(1)
        return prevRes.next


# @lc code=end
