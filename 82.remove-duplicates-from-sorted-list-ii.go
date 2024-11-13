/*
 * @lc app=leetcode id=82 lang=golang
 *
 * [82] Remove Duplicates from Sorted List II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
package main

/*
curr is current node, which move on linked list from left to right
prev, head
each iteration, (until curr is None)
if this node is repeating, find next different node
 1. connect prev to next diff node, move curr to next diff node and next iteration
 2. if no prev node, move head and curr to that next diff node

else

	move prev and curr
*/
func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	var prev *ListNode
	prev = nil
	ans := head
	curr := head
	for curr != nil {
		if curr.Next != nil && curr.Next.Val == curr.Val {
			nextDiffNode := curr.Next
			for nextDiffNode != nil && nextDiffNode.Val == curr.Val {
				nextDiffNode = nextDiffNode.Next
			}
			if prev != nil {
				prev.Next = nextDiffNode
				curr = nextDiffNode
			} else {
				ans = nextDiffNode
				curr = nextDiffNode
			}
		} else {
			prev = curr
			curr = curr.Next
		}
	}
	return ans
}

// @lc code=end
