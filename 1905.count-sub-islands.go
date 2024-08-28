/*
 * @lc app=leetcode id=1905 lang=golang
 *
 * [1905] Count Sub Islands
 */

// @lc code=start
package main

/*
  Run BFS for each island in grid2
  1. when running BFS, check if it's in grid 1. If not, stop counting and don't count it as sub island
*/

func countSubIslands(grid1 [][]int, grid2 [][]int) int {
	m := len(grid1)
	n := len(grid1[0])
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid2[i][j] == 0 || visited[i][j] {
				continue
			}
			// BFS
			isSubIsland := grid1[i][j] == 1
			queue := [][]int{{i, j}}
			visited[i][j] = true
			deltas := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
			for len(queue) > 0 {
				// pop queue
				x, y := queue[0][0], queue[0][1]
				queue = queue[1:]
				if grid1[x][y] == 0 {
					isSubIsland = false
				}
				for _, delta := range deltas {
					dx, dy := delta[0], delta[1]
					nx, ny := x+dx, y+dy
					if nx < 0 || nx >= m || ny < 0 || ny >= n {
						continue
					}
					if grid2[nx][ny] == 0 || visited[nx][ny] {
						continue
					}
					queue = append(queue, []int{nx, ny})
					visited[nx][ny] = true
				}
			}
			if isSubIsland {
				ans++
			}
		}
	}

	return ans
}

// @lc code=end
