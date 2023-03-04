#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# ref: https://abhisekbunty94.medium.com/why-does-floyds-cycle-detection-algorithm-work-59f61984dc3e#67a7
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return None
        slow, fast = head, head

        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
        

# @lc code=end

