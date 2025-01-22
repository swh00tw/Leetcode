/*
 * @lc app=leetcode id=1765 lang=golang
 *
 * [1765] Map of Highest Peak
 */

// @lc code=start
package main

type Point struct {
	X int
	Y int
}

func highestPeak(isWater [][]int) [][]int {
	/*
	   BFS from water,
	   then next batch,
	   end when all cell are visited
	*/
	m := len(isWater)
	n := len(isWater[0])
	hmap := make([][]int, m)
	for i, row := range isWater {
		hmap[i] = make([]int, n)
		for j, _ := range row {
			hmap[i][j] = -1
		}
	}
	deltas := [][]int{
		[]int{0, 1},
		[]int{1, 0},
		[]int{-1, 0},
		[]int{0, -1},
	}

	currHeight := 0
	batch := []Point{}
	for i, row := range isWater {
		for j, cell := range row {
			if cell == 1 {
				batch = append(batch, Point{i, j})
				hmap[i][j] = 0
			}
		}
	}
	for len(batch) > 0 {
		currHeight++
		nextBatch := []Point{}
		// pop all, push neighbor if not visited
		for _, p := range batch {
			for _, delta := range deltas {
				nx := p.X + delta[0]
				ny := p.Y + delta[1]
				if 0 <= nx && nx < m && 0 <= ny && ny < n && hmap[nx][ny] == -1 {
					hmap[nx][ny] = currHeight
					nextBatch = append(nextBatch, Point{nx, ny})
				}
			}
		}
		batch = nextBatch
	}
	return hmap
}

// @lc code=end
