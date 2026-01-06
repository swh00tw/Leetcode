package main

import "fmt"

// @leet start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type NodeLevelPair struct {
	Node  *TreeNode
	Level int
}

func maxLevelSum(root *TreeNode) int {
	if root == nil {
		return 0
	}
	ans := []int{1, root.Val} // level, val pair
	queue := []NodeLevelPair{}
	queue = append(queue, NodeLevelPair{Node: root, Level: 1})
	level2Sum := map[int]int{}
	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		level2Sum[curr.Level] += curr.Node.Val
		if curr.Node.Left != nil {
			queue = append(queue, NodeLevelPair{Node: curr.Node.Left, Level: curr.Level + 1})
		}
		if curr.Node.Right != nil {
			queue = append(queue, NodeLevelPair{Node: curr.Node.Right, Level: curr.Level + 1})
		}
		if len(queue) == 0 || (len(queue) > 0 && queue[0].Level != curr.Level) {
			if level2Sum[curr.Level] > ans[1] {
				fmt.Println(level2Sum[curr.Level], curr.Level)
				ans[0] = curr.Level
				ans[1] = level2Sum[curr.Level]
			}
		}
	}
	return ans[0]
}

// @leet end

