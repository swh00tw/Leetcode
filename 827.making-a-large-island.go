/*
 * @lc app=leetcode id=827 lang=golang
 *
 * [827] Making A Large Island
 */

// @lc code=start
package main

import (
	"fmt"
)

/*
Create a hashmap, map from cell to "the sum of nearby island"
For each island, run BFS, and for each boundary, increment the cell's value
*/

type Set[T comparable] map[T]bool

func (s Set[T]) Add(e T) {
	s[e] = true
}
func (s Set[T]) Has(e T) bool {
	_, ok := s[e]
	return ok
}
func (s Set[T]) ToArray() []T {
	ans := []T{}
	for k, _ := range s {
		ans = append(ans, k)
	}
	return ans
}

func largestIsland(grid [][]int) int {
	deltas := [][]int{
		[]int{0, -1},
		[]int{-1, 0},
		[]int{1, 0},
		[]int{0, 1},
	}
	toKey := func(x, y int) string {
		return fmt.Sprintf("%d,%d", x, y)
	}
	cell2Score := make(map[string]int)
	m := len(grid)
	n := len(grid[0])
	visited := make([][]bool, m)
	for i, _ := range grid {
		visited[i] = make([]bool, n)
	}
	ones := 0
	// BFS
	for i, row := range grid {
		for j, cell := range row {
			if cell == 1 {
				ones++
			}
			if cell == 0 || visited[i][j] {
				continue
			}
			bounds := Set[string]{}
			area := 0
			queue := [][]int{
				[]int{i, j},
			}
			visited[i][j] = true
			for len(queue) > 0 {
				// pop
				x, y := queue[0][0], queue[0][1]
				queue = queue[1:]
				area++
				// add neighbor, if in-bound
				for _, delta := range deltas {
					nx := x + delta[0]
					ny := y + delta[1]
					if nx >= 0 && nx < m && ny >= 0 && ny < n {
						if grid[nx][ny] == 1 {
							if visited[nx][ny] == false {
								visited[nx][ny] = true
								queue = append(queue, []int{nx, ny})
							}
						} else {
							bounds.Add(toKey(nx, ny))
						}
					}
				}
			}
			for _, cell := range bounds.ToArray() {
				cell2Score[cell] += area
			}
		}
	}

	if len(cell2Score) == 0 {
		// either no island or no empty cell
		if ones == m*n {
			return m * n
		}
		return 1
	}

	// select the best cell
	ans := 0
	for _, v := range cell2Score {
		if v > ans {
			ans = v
		}
	}
	return ans + 1
}

// @lc code=end
