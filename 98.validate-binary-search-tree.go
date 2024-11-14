/*
 * @lc app=leetcode id=98 lang=golang
 *
 * [98] Validate Binary Search Tree
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

import "math"

/*
define a recursive function validate(root *TreeNode, lower, upper int) bool {
 1. check if root in the bound
 2. left subtree should return true (validated)
 3. right subtree should return true
    Return 1 && 2 && 3
    }
*/
func isValidBST(root *TreeNode) bool {
	var validate func(root *TreeNode, lower, upper int) bool
	validate = func(root *TreeNode, lower, upper int) bool {
		if root == nil {
			return true
		}
		if root.Val <= lower || root.Val >= upper {
			return false
		}
		if !validate(root.Left, lower, root.Val) {
			return false
		}
		if !validate(root.Right, root.Val, upper) {
			return false
		}
		return true
	}

	return validate(root, -math.MaxInt, math.MaxInt)
}

// @lc code=end
