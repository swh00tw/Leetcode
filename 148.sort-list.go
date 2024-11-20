/*
 * @lc app=leetcode id=148 lang=golang
 *
 * [148] Sort List
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
Use merge sort,
Base case: the linked list length is 1 --> return
General case, find the middle point, divide into two list by removing the link
Merge two linked list and return
*/
func sortList(head *ListNode) *ListNode {
	n := 0
	curr := head
	for curr != nil {
		n++
		curr = curr.Next
	}

	if n <= 1 {
		return head
	}

	left := head
	var prev *ListNode
	right := head
	cnt := 0
	end := n / 2
	for cnt < end {
		prev = right
		right = right.Next
		cnt++
	}
	prev.Next = nil

	leftLL := sortList(left)
	rightLL := sortList(right)

	// merge
	if leftLL == nil {
		return rightLL
	} else if rightLL == nil {
		return leftLL
	}
	var l1 *ListNode
	var l2 *ListNode
	if leftLL.Val < rightLL.Val {
		l1 = leftLL
		l2 = rightLL
	} else {
		l1 = rightLL
		l2 = leftLL
	}

	p1 := l1
	p2 := l2
	for p2 != nil {
		// move p1 on l1 until we can't move forward
		val := p2.Val
		for p1 != nil && p1.Next != nil {
			if p1.Next.Val <= val {
				p1 = p1.Next
			} else {
				break
			}
		}
		// insert node
		nextP2 := p2.Next
		p2.Next = nil
		nextP1 := p1.Next
		p1.Next = p2
		p2.Next = nextP1
		// update p1 and p2
		p2 = nextP2
		p1 = p1.Next
	}
	return l1
}

// @lc code=end
