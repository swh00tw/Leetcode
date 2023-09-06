#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size = 1
        else:
            self.tail.next = node
            self.tail = self.tail.next
            self.size += 1


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        sizes = [length // k] * k
        left = length % k
        idx = 0
        while left > 0:
            sizes[idx] += 1
            left -= 1
            idx += 1

        ans = []
        curr = head
        currGroupIdx = 0
        currLL = LinkedList()
        while curr:
            nextNode = curr.next
            curr.next = None
            if currLL.size == sizes[currGroupIdx]:
                ans.append(currLL.head)
                currLL = LinkedList()
                currGroupIdx += 1
            currLL.add(curr)
            curr = nextNode
        ans.append(currLL.head)
        while len(ans) < k:
            ans.append(None)
        return ans


# @lc code=end
