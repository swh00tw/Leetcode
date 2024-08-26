/*
 * @lc app=leetcode id=590 lang=golang
 *
 * [590] N-ary Tree Postorder Traversal
 */

// @lc code=start
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */
func postorder(root *Node) []int {
	if root == nil {
		return []int{}
	}
	children := make([]int, 0)
	for _, n := range root.Children {
		children = append(children, postorder(n)...)
	}
	return append(children, root.Val)
}

// @lc code=end

