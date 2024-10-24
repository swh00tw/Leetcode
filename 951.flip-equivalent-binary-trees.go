/*
 * @lc app=leetcode id=951 lang=golang
 *
 * [951] Flip Equivalent Binary Trees
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
package main

/*
  for each node, it's equivalent if
  1. root value is the same
  2. flip or not flip
*/

func flipEquiv(root1 *TreeNode, root2 *TreeNode) bool {
	if root1 == nil && root2 == nil {
		return true
	}
	if root1 == nil || root2 == nil {
		return false
	}
	// required condition
	if root1.Val != root2.Val {
		return false
	}
	resNotFlip := flipEquiv(root1.Left, root2.Left) && flipEquiv(root1.Right, root2.Right)
	resFlip := flipEquiv(root1.Left, root2.Right) && flipEquiv(root1.Right, root2.Left)
	return resNotFlip || resFlip
}

// @lc code=end
