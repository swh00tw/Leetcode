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
        n1 = l1
        n2 = l2
        res = ListNode()
        tail = res
        addOne = False
        while n1 or n2:
            # add n1 and n2, generate a new Node
            newNode, addOne = self.addTwoNode(n1, n2, addOne)
            # append to tail, update tail
            tail.next = newNode
            tail = tail.next
            # update n1, n2
            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None
        # if addOne is true, append last node
        if addOne:
            tail.next = ListNode(1)
        return res.next

    def addTwoNode(
        self, n1: Optional[ListNode], n2: Optional[ListNode], addOne=False
    ) -> Optional[ListNode]:
        if not n1 and not n2:
            return None
        val1 = n1.val if n1 is not None else 0
        val2 = n2.val if n2 is not None else 0
        newVal = val1 + val2 + (1 if addOne else 0)
        return ListNode(newVal % 10), (newVal // 10 == 1)


# @lc code=end
