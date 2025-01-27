/*
 * @lc app=leetcode id=1462 lang=golang
 *
 * [1462] Course Schedule IV
 */

// @lc code=start
package main

import "fmt"

/*
 1. build adj list
 2. write a func isReachable(v, u int) bool
    the function is cached
 3. return ans
*/
func checkIfPrerequisite(numCourses int, prerequisites [][]int, queries [][]int) []bool {
	adjList := make(map[int][]int)
	for i := 0; i < numCourses; i++ {
		adjList[i] = []int{}
	}
	for _, pair := range prerequisites {
		src, dst := pair[0], pair[1]
		adjList[src] = append(adjList[src], dst)
	}

	cache := make(map[string]bool)
	toKey := func(u, v int) string {
		return fmt.Sprintf("%d,%d", u, v)
	}
	var isReachable func(u, v int) bool
	isReachable = func(u, v int) bool {
		// in cache
		key := toKey(u, v)
		if res, ok := cache[key]; ok {
			return res
		}
		// edge case
		if u == v {
			return true
		}
		ans := false
		for _, n := range adjList[u] {
			if isReachable(n, v) {
				ans = true
				break
			}
		}
		// update cache
		cache[key] = ans
		return ans
	}

	ans := []bool{}
	for _, q := range queries {
		ans = append(ans, isReachable(q[0], q[1]))
	}
	return ans
}

// @lc code=end
