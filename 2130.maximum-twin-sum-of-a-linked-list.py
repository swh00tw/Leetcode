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
        # need to know "n" first
        # use an array of n/2 to store twin sums
        slow = head
        fast = head
        twin_sums = []
        while fast and fast.next:
            twin_sums.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        n = len(twin_sums)
        ans = float("-inf")
        while slow:
            n = twin_sums.pop()
            ans = max(ans, n + slow.val)
            slow = slow.next
        return ans


# @lc code=end
