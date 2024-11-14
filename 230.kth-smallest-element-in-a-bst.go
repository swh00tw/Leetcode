/*
 * @lc app=leetcode id=230 lang=golang
 *
 * [230] Kth Smallest Element in a BST
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthSmallest(root *TreeNode, k int) int {
	vals := inorder(root)
	return vals[k-1]
}

func inorder(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	return append(append(inorder(root.Left), root.Val), inorder(root.Right)...)
}

// @lc code=end

