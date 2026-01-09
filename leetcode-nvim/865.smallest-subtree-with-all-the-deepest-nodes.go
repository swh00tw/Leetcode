package main

// @leet start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
	// base answer, if root is nil, answer is root
	// else, if deepest(node.left) == deepest(node.right), ans is node
	// if deepest(node.left) > deepest(node.right), ans is node.left

	cache := map[*TreeNode]int{}
	var getDepth func(node *TreeNode) int
	getDepth = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		if v, ok := cache[node]; ok {
			return v
		}
		ans := max(getDepth(node.Left), getDepth(node.Right)) + 1
		cache[node] = ans
		return ans
	}

	var getAns func(node *TreeNode) *TreeNode
	getAns = func(node *TreeNode) *TreeNode {
		l, r := getDepth(node.Left), getDepth(node.Right)
		if l == r {
			return node
		} else if l >= r {
			return getAns(node.Left)
		}
		return getAns(node.Right)
	}

	return getAns(root)
}

// @leet end

