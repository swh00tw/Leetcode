/*
 * @lc app=leetcode id=2326 lang=golang
 *
 * [2326] Spiral Matrix IV
 */

// @lc code=start
package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
var deltas [][]int = [][]int{
	[]int{0, 1},
	[]int{1, 0},
	[]int{0, -1},
	[]int{-1, 0},
}

func spiralMatrix(m int, n int, head *ListNode) [][]int {
	/*
	   1. make the matrix and fill with -1
	   2. fill the matrix
	*/
	mat := make([][]int, m)
	for i := 0; i < m; i++ {
		mat[i] = make([]int, n)
		for j := 0; j < n; j++ {
			mat[i][j] = -1
		}
	}

	direction := 0 // 0, 1, 2, 3: right, down, left, up
	curr := head
	pos := []int{0, 0}
	for curr != nil {
		x, y := pos[0], pos[1]
		mat[x][y] = curr.Val
		curr = curr.Next
		nextPos, hasTurn := getNextPos(pos, mat, direction)
		pos = nextPos
		if hasTurn {
			direction = turnRight(direction)
		}
	}
	return mat
}

func turnRight(dir int) int {
	return (dir + 1) % 4
}

func getNextPos(curr []int, mat [][]int, dir int) ([]int, bool) {
	m := len(mat)
	n := len(mat[0])
	x, y := curr[0], curr[1]
	delta := deltas[dir]
	nx := x + delta[0]
	ny := y + delta[1]
	if 0 <= nx && nx < m && 0 <= ny && ny < n && mat[nx][ny] == -1 {
		return []int{nx, ny}, false
	}
	nextDir := turnRight(dir)
	nx = x + deltas[nextDir][0]
	ny = y + deltas[nextDir][1]
	return []int{nx, ny}, true
}

// @lc code=end
