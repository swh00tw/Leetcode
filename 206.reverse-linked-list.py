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
        if head == None or head.next == None:
            return head
        nodes = []
        curr = head
        while curr:
            new = ListNode(curr.val)
            nodes.append(new)
            curr = curr.next
        revNodes = list(reversed(nodes))

        headOfRevNodes = revNodes[0]
        for i in range(len(revNodes)-1):
            current = revNodes[i]
            current.next = revNodes[i+1]
        return headOfRevNodes
        
        
            
        
# @lc code=end

