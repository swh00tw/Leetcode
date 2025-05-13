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
func lcaDeepestLeaves(root *TreeNode) *TreeNode {
	// create a recursive func(node), return len of the path from curr to the deepest leaves, and lca
	// base case: if reach nil node, return 0, nil
	// else, if the length of left and right subtrees is the same, lca is curr node, return length+1, curr
	// if left is deeper, return answer from left
	// if right is deeper, return answer from right
	var getDeepestLeavesLca func(node *TreeNode) (int, *TreeNode)
	getDeepestLeavesLca = func(node *TreeNode) (int, *TreeNode) {
		if node == nil {
			return 0, nil
		}
		leftLen, leftLca := getDeepestLeavesLca(node.Left)
		rightLen, rightLca := getDeepestLeavesLca(node.Right)
		if leftLen == rightLen {
			return leftLen + 1, node
		}
		if leftLen > rightLen {
			return leftLen + 1, leftLca
		}
		return rightLen + 1, rightLca
	}

	_, node := getDeepestLeavesLca(root)
	return node
}

// @leet end
