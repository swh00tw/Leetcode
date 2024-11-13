/*
 * @lc app=leetcode id=86 lang=golang
 *
 * [86] Partition List
 */

// @lc code=start
package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
recursively
*/
func partition(head *ListNode, x int) *ListNode {
	// base case
	if head == nil {
		return head
	}
	if head.Next == nil {
		return head
	}
	subans := partition(head.Next, x)
	// two cases,
	// if head is lower than x, just stay at front and return head -> subans
	// else, go thru subans and insert head to the right place, find the last item that lower than x, and insert it at its behind
	if head.Val < x {
		head.Next = subans
		return head
	}
	var prev *ListNode = nil
	curr := subans
	for curr != nil && curr.Val < x {
		prev = curr
		curr = curr.Next
	}
	if prev == nil {
		head.Next = subans
		return head
	}
	nextNode := prev.Next
	prev.Next = head
	head.Next = nextNode
	return subans
}

// @lc code=end
