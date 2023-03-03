#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        
        middle = length//2
        curr = head
        while middle>0:
            curr = curr.next
            middle -= 1
        return curr
    
# other sol: https://leetcode.com/problems/middle-of-the-linked-list/solutions/1651600/python-java-c-simple-solution-one-pass-beginner-friendly-detailed-explanation/?envType=study-plan&id=level-1
        
# @lc code=end

