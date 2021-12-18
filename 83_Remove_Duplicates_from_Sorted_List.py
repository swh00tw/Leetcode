# easy
# O(n)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        val_d = {}
        now = head
        prev = None
        while now:
            if (now.val in val_d):
                prev.next = now.next
                now = now.next
            else:
                val_d[now.val]=1
                prev = now
                now = now.next
        return head
            