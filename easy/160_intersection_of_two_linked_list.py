# easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        # count the length of each linked list
        length_a = 0
        length_b = 0
        curr_a = headA
        curr_b = headB
        while curr_a:
            length_a+=1
            curr_a = curr_a.next
        while curr_b:
            length_b+=1
            curr_b = curr_b.next
            
        # init
        curr_a = headA
        curr_b = headB
        # align two linked list head first
        # after aligned,
        # if two pointer point to the same node, return answer
        # else, check next node in both lists
        while length_a>0 and length_b>0:
            if (length_a>length_b):
                length_a-=1
                curr_a = curr_a.next
            elif (length_b>length_a):
                length_b-=1
                curr_b = curr_b.next
            else:
                if (curr_a==curr_b):
                    return curr_a
                else:
                    length_a-=1
                    length_b-=1
                    curr_a = curr_a.next
                    curr_b = curr_b.next
        return None