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
        ans = ListNode(0)
        ans.next = head
        # stand on curr node
        # if there are k nodes after this node (need count)
        # reverse it (return head, nextHead), and relink the pointers
        curr = ans
        while self.countK(curr, k):
            new_head, new_tail, next_head = self.reverseKNodes(curr.next, k)
            curr.next = new_head
            new_tail.next = next_head
            curr = new_tail
        return ans.next

    def countK(self, node, k) -> bool:
        c = 0
        curr = node.next
        while curr:
            c += 1
            curr = curr.next
            if c == k:
                return True
        return False

    def reverseKNodes(self, node, k):
        # return head, tail, nextHead
        # base case: k == 1
        new_node = ListNode(node.val)
        if k == 1:
            return new_node, new_node, node.next

        head, tail, next_head = self.reverseKNodes(node.next, k - 1)
        tail.next = new_node
        return head, tail.next, next_head


# @lc code=end
