/*
 * @lc app=leetcode id=725 lang=golang
 *
 * [725] Split Linked List in Parts
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
func splitListToParts(head *ListNode, k int) []*ListNode {
	if head == nil {
		return make([]*ListNode, k)
	}
	// count and calculate for each sub linked lists
	n := 0
	curr := head
	for curr != nil {
		n++
		curr = curr.Next
	}
	nodes := make([]int, k)
	base := n / k
	remainder := n % k
	for i := 0; i < k; i++ {
		nodes[i] = base
		if remainder > 0 {
			nodes[i]++
			remainder--
		}
	}
	// prepare answer
	ans := make([]*ListNode, k)
	var prev *ListNode = nil
	curr = head
	for i := 0; i < k; i++ {
		ans[i] = curr
		x := nodes[i]
		// move curr x times
		for j := 0; j < x; j++ {
			if curr != nil {
				prev = curr
				curr = curr.Next
			}
		}
		// split
		prev.Next = nil
	}
	return ans
}

// @lc code=end
