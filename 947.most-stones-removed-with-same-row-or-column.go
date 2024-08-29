/*
 * @lc app=leetcode id=947 lang=golang
 *
 * [947] Most Stones Removed with Same Row or Column
 */

// @lc code=start
package main

/*
  make it a graph problem
  1. run DFS/BFS, there is an edge for any node (a, b) is other nodes on x=a or y=b
  keep track of how many time we run DFS, we can get the answer
  since if a node can be visited by DFS, it means that can be removed
  2. use UnionFind, the edges are x = a, b, c, ..., y = i, j, k, ...
*/

func removeStones(stones [][]int) int {
	setX := make(map[int][][]int)
	setY := make(map[int][][]int)
	for i, coordinate := range stones {
		x, y := coordinate[0], coordinate[1]
		if setX[x] == nil {
			setX[x] = make([][]int, 0)
		}
		if setY[y] == nil {
			setY[y] = make([][]int, 0)
		}
		setX[x] = append(setX[x], []int{x, y, i})
		setY[y] = append(setY[y], []int{x, y, i})
	}

	visited := make([]bool, len(stones))
	bfs := 0
	queue := [][]int{}
	for i, stone := range stones {
		if visited[i] {
			continue
		}
		bfs++
		queue = append(queue, []int{stone[0], stone[1], i})
		visited[i] = true
		for len(queue) > 0 {
			node := queue[0]
			queue = queue[1:]
			for _, neighbor := range setX[node[0]] {
				idx := neighbor[2]
				if !visited[idx] {
					visited[idx] = true
					queue = append(queue, neighbor)
				}
			}
			for _, neighbor := range setY[node[1]] {
				idx := neighbor[2]
				if !visited[idx] {
					visited[idx] = true
					queue = append(queue, neighbor)
				}
			}
		}
	}
	return len(stones) - bfs
}

// @lc code=end
