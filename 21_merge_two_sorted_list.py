# easy
# O(n)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        i=list1
        j=list2
        res=ListNode(0,None)
        head=res
        while (i!=None or j!=None):
            # special case
            if (i==None):
                res.next=j
                break
            if (j==None):
                res.next=i
                break
            # main logic
            if (i.val<=j.val):
                res.next=i
                i=i.next
            else:
                res.next=j
                j=j.next
            res=res.next
        return head.next