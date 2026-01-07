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

const MOD = 1000000007

func maxProduct(root *TreeNode) int {
	// need to memorize the sum of a subtree
	// use a map map from pointer to TreeNode to sum
	// traverse each node, try to cut a edge, we can get the product by multiple sum of subtree x and (sum of root - x)
	node2Sum := map[*TreeNode]int{}
	var getSum func(node *TreeNode) int
	getSum = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		ans := node.Val + getSum(node.Left) + getSum(node.Right)
		node2Sum[node] = ans
		return ans
	}
	rootSum := getSum(root)
	ans := 0
	var visit func(node *TreeNode)
	visit = func(node *TreeNode) {
		if node.Left != nil {
			x := node2Sum[node.Left]
			ans = max(ans, (rootSum-x)*x)
			visit(node.Left)
		}
		if node.Right != nil {
			x := node2Sum[node.Right]
			ans = max(ans, (rootSum-x)*x)
			visit(node.Right)
		}
	}
	visit(root)
	return ans % MOD
}

// @leet end

