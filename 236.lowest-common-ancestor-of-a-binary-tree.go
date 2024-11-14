/*
 * @lc app=leetcode id=236 lang=golang
 *
 * [236] Lowest Common Ancestor of a Binary Tree
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
 0. if node is nil, return nil
 1. p is root -> return p
 2. q is root -> return q
 3. neither p nor q is root
    a. two of them are in left tree -> if got nil, means two nodes in right tree, return right answer
    b. two of them are in right tree -> if got nil, means two nodes in left tree, return left answer
    c. if not the above cases (both answer return a node), return root
*/
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Val == p.Val {
		return p
	}
	if root.Val == q.Val {
		return q
	}
	leftAns := lowestCommonAncestor(root.Left, p, q)
	rightAns := lowestCommonAncestor(root.Right, p, q)
	if leftAns == nil {
		return rightAns
	}
	if rightAns == nil {
		return leftAns
	}
	return root
}

// @lc code=end
