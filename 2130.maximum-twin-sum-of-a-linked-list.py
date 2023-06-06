#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        fast = head
        res = -inf
        stack = []
        while fast and fast.next:
            stack.append(curr.val)
            curr = curr.next
            fast = fast.next.next
        while curr:
            res = max(res, curr.val+stack.pop())
            curr = curr.next
        return res

        
# @lc code=end

