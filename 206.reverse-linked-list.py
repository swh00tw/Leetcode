#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        self.res = None

        # backtracking
        def getRevLinkedList(originalNode):
            node = ListNode(originalNode.val)

            if originalNode.next is None:
                self.res = node
                return node
            tailNode = getRevLinkedList(originalNode.next)
            tailNode.next = node
            return tailNode.next

        getRevLinkedList(head)
        return self.res


# @lc code=end
