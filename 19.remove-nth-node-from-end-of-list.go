/*
 * @lc app=leetcode id=19 lang=golang
 *
 * [19] Remove Nth Node From End of List
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
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	total := 0
	curr := head
	for curr != nil {
		total++
		curr = curr.Next
	}
	idx := total - n // idx to remove
	if idx == 0 {
		return head.Next
	}
	i := 0
	var prev *ListNode
	curr = head
	for i <= idx {
		if i == idx {
			prev.Next = curr.Next
			curr.Next = nil
		}
		prev = curr
		curr = curr.Next
		i++
	}
	return head
}

// @lc code=end
