/*
 * @lc app=leetcode id=530 lang=golang
 *
 * [530] Minimum Absolute Difference in BST
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

func getMinimumDifference(root *TreeNode) int {
	nodeVals := inorder(root)
	minDiff := math.MaxInt
	n := len(nodeVals)
	for i := 0; i < n-1; i++ {
		diff := nodeVals[i+1] - nodeVals[i]
		if diff < minDiff {
			minDiff = diff
		}
	}
	return minDiff
}

func inorder(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	return append(append(inorder(root.Left), root.Val), inorder(root.Right)...)
}

// @lc code=end
