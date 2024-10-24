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

/*
maintain a stack of *TreeNode
Next() just pop the top item of the stack and push if it has right child (and the leftmost child)
HasNext(), if the stack is not empty, return true, otherwis, false
*/
type BSTIterator struct {
	stack []*TreeNode
}

func pushRightSubtree(currStack []*TreeNode, root *TreeNode) []*TreeNode {
	nodes := make([]*TreeNode, 0)
	curr := root
	for curr != nil {
		nodes = append(nodes, curr)
		curr = curr.Left
	}
	newStack := append(currStack, nodes...)
	return newStack
}

func Constructor(root *TreeNode) BSTIterator {
	initStack := make([]*TreeNode, 0)
	nodes := pushRightSubtree(initStack, root)
	return BSTIterator{
		stack: nodes,
	}
}

func (this *BSTIterator) Next() int {
	// pop item from stack
	node := this.stack[len(this.stack)-1]
	this.stack = this.stack[:len(this.stack)-1]
	// append right subtree
	this.stack = pushRightSubtree(this.stack, node.Right)
	return node.Val
}

func (this *BSTIterator) HasNext() bool {
	return len(this.stack) > 0
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
// @lc code=end
