#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Linear traverse
        # 1. select a group. (if lower than k nodes, early return)
        # 2. modify the pointers
        if k == 1:
            return head
        prev = None
        curr = head
        res = head
        while self.countNodes(curr) >= k:
            tail, head, nextCurr = self.reverseNodes(curr, 1, k)
            tail.next = nextCurr
            # print("tail: ", tail, "next: ", nextCurr)
            if prev is not None:
                prev.next = head
            else:
                res = head
            # update prev and update curr
            prev = curr
            curr = nextCurr

        return res

    def countNodes(self, head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def reverseNodes(self, node, idx, k):
        if idx == k:
            return node, node, node.next
        tail, head, nextCurr = self.reverseNodes(node.next, idx + 1, k)
        tail.next = node
        tail = tail.next
        return tail, head, nextCurr


# @lc code=end
