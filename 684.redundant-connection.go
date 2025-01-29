/*
 * @lc app=leetcode id=684 lang=golang
 *
 * [684] Redundant Connection
 */

// @lc code=start
package main

/*
  use UnionFind
*/

type UnionFind struct {
	n    int
	root []int
	rank []int
}

func getNewUf(n int) *UnionFind {
	root := make([]int, n)
	rank := make([]int, n)
	for i := 0; i < n; i++ {
		root[i] = i
		rank[i] = 1
	}
	uf := UnionFind{
		n:    n,
		root: root,
		rank: rank,
	}
	return &uf
}

func (uf *UnionFind) Find(x int) int {
	if uf.root[x] != x {
		uf.root[x] = uf.Find(uf.root[x])
	}
	return uf.root[x]
}

func (uf *UnionFind) Union(x, y int) bool {
	rx := uf.Find(x)
	ry := uf.Find(y)
	if rx == ry {
		return false
	}
	if uf.rank[rx] == uf.rank[ry] {
		uf.root[rx] = ry
		uf.rank[ry]++
	} else if uf.rank[rx] > uf.rank[ry] {
		uf.root[ry] = rx
	} else {
		uf.root[rx] = ry
	}
	return true
}

func findRedundantConnection(edges [][]int) []int {
	n := len(edges)
	uf := getNewUf(n)

	for _, edge := range edges {
		src, dst := edge[0]-1, edge[1]-1 // from 1-indexed to 0-indexed
		res := uf.Union(src, dst)
		if res == false {
			return edge
		}
	}
	return []int{0, 0}
}

// @lc code=end
