/*
 * @lc app=leetcode id=108 lang=golang
 *
 * [108] Convert Sorted Array to Binary Search Tree
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
recursive
base case: if len is zero
general case: get the middle one and make it a node, finish left tree and right tree and concat them, return root
*/
func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	l := 0
	r := len(nums) - 1
	m := (l + r) / 2
	root := TreeNode{
		Val:   nums[m],
		Left:  sortedArrayToBST(nums[:m]),
		Right: sortedArrayToBST(nums[m+1:]),
	}
	return &root
}

// @lc code=end
