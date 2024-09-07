/*
 * @lc app=leetcode id=1367 lang=golang
 *
 * [1367] Linked List in Binary Tree
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
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubPath(head *ListNode, root *TreeNode) bool {
	// recursive
	// if this node == head
	// return isSubPath(head.next, root.Left) or isSubPath(head.next, root.Right)
	// else, find left and right subtree
	// base case, head == nil or root == nil
	if root == nil {
		return false
	}
	return hasSubPath(head, root) || isSubPath(head, root.Left) || isSubPath(head, root.Right)
}

func hasSubPath(curr *ListNode, node *TreeNode) bool {
	if curr == nil {
		return true
	}
	if node == nil {
		return false
	}
	if curr.Val != node.Val {
		return false
	}
	return hasSubPath(curr.Next, node.Left) || hasSubPath(curr.Next, node.Right)
}

// @lc code=end
