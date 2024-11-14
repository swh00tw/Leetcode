/*
 * @lc app=leetcode id=114 lang=golang
 *
 * [114] Flatten Binary Tree to Linked List
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
recursively call flatten
for each tree root,
1. call flatten on its left subtree
2. call flatten on its right subtree
4. append the right subtree (right linked list) behind the left subtree (if right tree is not nil)
3. move left linked list (left subtree) to right child
4. set left child to null

base cases
1. root is nil -> return nil
*/
func flatten(root *TreeNode) {
	if root == nil {
		return
	}
	flatten(root.Left)
	flatten(root.Right)
	if root.Right != nil {
		if root.Left == nil {
			root.Left = root.Right
		} else {
			// find the tail of left list
			curr := root.Left
			for curr != nil && curr.Right != nil {
				curr = curr.Right
			}
			curr.Right = root.Right
		}
	}
	root.Right = root.Left
	root.Left = nil
}

// @lc code=end
