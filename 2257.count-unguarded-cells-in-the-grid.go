/*
 * @lc app=leetcode id=2257 lang=golang
 *
 * [2257] Count Unguarded Cells in the Grid
 */

// @lc code=start
package main

import "fmt"

/*
calculate total grids - walls - guards
for each guard, start propagating in 4 directions
*/
type Grid struct {
	m          int
	n          int
	visited    [][]bool
	visitedCnt int
	wallsSet   map[string]bool
	guards     [][]int
	guardsSet  map[string]bool
}

func positionToKey(pos []int) string {
	x, y := pos[0], pos[1]
	return fmt.Sprintf("%d,%d", x, y)
}

func generateGrid(m, n int, guards [][]int, walls [][]int) *Grid {
	visitedCnt := 0
	visitedCnt += len(guards)
	visitedCnt += len(walls)
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}

	wallsSet := make(map[string]bool)
	for _, w := range walls {
		key := positionToKey(w)
		wallsSet[key] = true

		visited[w[0]][w[1]] = true
	}
	guardsSet := make(map[string]bool)
	for _, g := range guards {
		key := positionToKey(g)
		guardsSet[key] = true
		visited[g[0]][g[1]] = true
	}

	grid := Grid{
		m:          m,
		n:          n,
		visited:    visited,
		visitedCnt: visitedCnt,
		wallsSet:   wallsSet,
		guards:     guards,
		guardsSet:  guardsSet,
	}
	return &grid
}

func (g *Grid) Propagate(startPos []int) {
	deltas := [][]int{
		[]int{0, 1},
		[]int{1, 0},
		[]int{0, -1},
		[]int{-1, 0},
	}

	for _, delta := range deltas {
		dx := delta[0]
		dy := delta[1]
		// while loop until reach boundary or wall
		curr := []int{
			startPos[0] + dx,
			startPos[1] + dy,
		}
		for {
			// if meet wall
			key := positionToKey(curr)
			if g.wallsSet[key] {
				break
			}
			// if meet guard
			if g.guardsSet[key] {
				break
			}
			// if out of bound
			x := curr[0]
			y := curr[1]
			if x < 0 || x >= g.m || y < 0 || y >= g.n {
				break
			}
			// else, updating curr to next by dx dy
			// if not visited, mark visited and increment cnt
			if g.visited[x][y] == false {
				g.visited[x][y] = true
				g.visitedCnt++
			}
			curr = []int{
				x + dx,
				y + dy,
			}
		}
	}
}

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
	grid := generateGrid(m, n, guards, walls)
	for _, g := range guards {
		grid.Propagate(g)
	}
	return m*n - grid.visitedCnt
}

// @lc code=end
