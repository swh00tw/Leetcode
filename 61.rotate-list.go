/*
 * @lc app=leetcode id=61 lang=golang
 *
 * [61] Rotate List
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
count the length of the list, rotate = rotate % n
connect tail to head, calculate the position of new head and new tail, break the link between them
return new head
*/
func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}
	n := 0
	curr := head
	for {
		n++
		if curr.Next == nil {
			break
		}
		curr = curr.Next
	}
	rotate := k % n
	if rotate == 0 {
		return head
	}
	curr.Next = head

	target := n - rotate
	prev := curr
	curr = head
	i := 0
	for i != target {
		prev = curr
		curr = curr.Next
		i++
	}
	prev.Next = nil
	return curr
}

// @lc code=end
