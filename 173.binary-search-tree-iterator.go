/*
 * @lc app=leetcode id=173 lang=golang
 *
 * [173] Binary Search Tree Iterator
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

type BSTIterator struct {
	values  []int
	currIdx int
}

func Constructor(root *TreeNode) BSTIterator {
	// perform inorder traversal
	values := []int{}
	var visit func(node *TreeNode)
	visit = func(node *TreeNode) {
		if node == nil {
			return
		}
		visit(node.Left)
		values = append(values, node.Val)
		visit(node.Right)
	}
	visit(root)
	return BSTIterator{
		values:  values,
		currIdx: 0,
	}
}

func (this *BSTIterator) Next() int {
	idx := this.currIdx
	this.currIdx++
	return this.values[idx]
}

func (this *BSTIterator) HasNext() bool {
	return this.currIdx < len(this.values)
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
// @lc code=end
