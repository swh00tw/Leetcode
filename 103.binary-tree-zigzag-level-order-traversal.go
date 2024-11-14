/*
 * @lc app=leetcode id=103 lang=golang
 *
 * [103] Binary Tree Zigzag Level Order Traversal
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
define a recursive function: visitLevel(nodes []*TreeNode, leftToRight bool)
if leftToRight is true, this level should be traverse left to right, else right to left

visitLevel(nodes, leftToRight){

 1. traverse this level in the order specified by the 2nd parameter

 2. return [thisLevelTraversalOutput, visitLevel(nodesAtNextLevel)...]

    base case, if curr level, no nodes, return []
    }

return visitLevel([root], true)
*/
func zigzagLevelOrder(root *TreeNode) [][]int {

	var visitLevel func(nodes []*TreeNode, l2r bool) [][]int
	visitLevel = func(nodes []*TreeNode, l2r bool) [][]int {
		if len(nodes) == 0 {
			return [][]int{}
		}
		currLevel := make([]int, len(nodes))
		if l2r == true {
			for i, n := range nodes {
				currLevel[i] = n.Val
			}
		} else {
			for i, n := range nodes {
				currLevel[len(nodes)-1-i] = n.Val
			}
		}
		nextLevel := []*TreeNode{}
		for _, n := range nodes {
			if n.Left != nil {
				nextLevel = append(nextLevel, n.Left)
			}
			if n.Right != nil {
				nextLevel = append(nextLevel, n.Right)
			}
		}
		ans := [][]int{
			currLevel,
		}
		ans = append(ans, visitLevel(nextLevel, !l2r)...)
		return ans
	}
	if root == nil {
		return [][]int{}
	}
	return visitLevel([]*TreeNode{root}, true)
}

// @lc code=end
