/*
 * @lc app=leetcode id=199 lang=golang
 *
 * [199] Binary Tree Right Side View
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
BFS
levelVal = [], levelVal[i] == the rightmost node's val at i-th level
q = [(node, level), ...]
when we pop an item, we  update levelVal[level] use val node.Val
and push next level node to the queue (left to right)
*/
type NodeAndLevel struct {
	node  *TreeNode
	level int
}

func rightSideView(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	queue := make([]NodeAndLevel, 0)
	queue = append(queue, NodeAndLevel{
		node:  root,
		level: 0,
	})
	levelVal := []int{}
	for len(queue) > 0 {
		// pop
		nodeLevel := queue[0]
		queue = queue[1:]
		node := nodeLevel.node
		level := nodeLevel.level
		// update levelVal
		if len(levelVal) == level {
			levelVal = append(levelVal, node.Val)
		} else {
			levelVal[level] = node.Val
		}
		// append children to queue
		if node.Left != nil {
			queue = append(queue, NodeAndLevel{
				node:  node.Left,
				level: level + 1,
			})
		}
		if node.Right != nil {
			queue = append(queue, NodeAndLevel{
				node:  node.Right,
				level: level + 1,
			})
		}
	}
	return levelVal
}

// @lc code=end
