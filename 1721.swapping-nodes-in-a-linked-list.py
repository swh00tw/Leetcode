#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        nodes = []
        leftNode = None
        curr = head
        idx = 1
        while curr:
            if idx == k:
                leftNode = curr
            nodes.append(curr)
            idx+=1
            curr = curr.next
        rightNode = nodes[len(nodes)-k]
        rightNode.val, leftNode.val = leftNode.val, rightNode.val
        return head
        
# @lc code=end

