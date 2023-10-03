#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class HeapNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def __lt__(self, other):
        if other:
            return self.val < other.val
        return False

    def __eq__(self, other):
        if other:
            return self.val == other.val
        return False


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # handle edge case when len(lists) is 0
        # head of linked list could be None
        # filter out those linked list, if the length of lists is zero, early return
        # use k pointers point to current node (initially point to head)
        # they are candidates to be next node of resulting linked list
        # from k candidates, pick the smallest node to be next node
        # O(k) to do this, there are at most O(kn) time to do this
        # by maintain a minHeap, extract minimum can be done in O(lgn)
        # push a new candidate into heap is also O(lgn)
        new_lists = []
        for head in lists:
            if head is not None:
                new_lists.append(head)
        lists = new_lists
        if len(lists) == 0:
            return None

        n = len(lists)
        candidates = []  # store HeapNode
        for i, head in enumerate(lists):
            candidates.append(HeapNode(head.val, head.next))
        heapq.heapify(candidates)

        head = ListNode()
        curr = head
        while candidates:
            # extract minimum from candidate
            heapNode = heapq.heappop(candidates)
            val = heapNode.val
            nextNode = heapNode.next
            if nextNode:
                heapq.heappush(candidates, HeapNode(nextNode.val, nextNode.next))
            newNode = ListNode(val=val)
            curr.next = newNode
            curr = curr.next

        return head.next


# @lc code=end
