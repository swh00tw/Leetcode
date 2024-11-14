/*
 * @lc app=leetcode id=129 lang=golang
 *
 * [129] Sum Root to Leaf Numbers
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
we can define a recursive function: visit(node *TreeNode, acc int)
keep DFS or BFS, when visiting leaf node -> increment the answer by path sum
at each level, path sum is updated like this, curr node val + 10*acc
*/
func sumNumbers(root *TreeNode) int {
	ans := 0

	var visit func(node *TreeNode, acc int)
	visit = func(node *TreeNode, acc int) {
		newAcc := acc*10 + node.Val
		// base case
		if node.Left == nil && node.Right == nil {
			ans += newAcc
			return
		}
		if node.Left != nil {
			visit(node.Left, newAcc)
		}
		if node.Right != nil {
			visit(node.Right, newAcc)
		}
	}
	visit(root, 0)
	return ans
}

// @lc code=end
