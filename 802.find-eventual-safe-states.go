/*
 * @lc app=leetcode id=802 lang=golang
 *
 * [802] Find Eventual Safe States
 */

// @lc code=start
package main

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

func eventualSafeNodes(graph [][]int) []int {
	/*
	   safe node: node cycle found if do BFS or DFS
	*/
	cache := make(map[int]bool)
	visited := make([]bool, len(graph))
	cycleNodes := Set[int]{}
	var visit func(idx int) bool // return found cycle or no
	visit = func(idx int) bool {
		if res, ok := cache[idx]; ok {
			return res
		}
		// edge case
		if visited[idx] {
			cycleNodes.Add(idx)
			return true
		}
		neighbors := graph[idx]
		if len(neighbors) == 0 {
			return false
		}

		found := false
		visited[idx] = true
		for _, nei := range neighbors {
			subans := visit(nei)
			if subans == true {
				cycleNodes.Add(idx)
			}
			found = found || subans
		}
		visited[idx] = false

		cache[idx] = found
		return found
	}

	ans := []int{}
	for i, _ := range graph {
		if cycleNodes.Has(i) {
			continue
		}
		res := visit(i)
		if res == false {
			ans = append(ans, i)
		}
	}
	return ans
}

// @lc code=end
