package main

// @leet start
// sol: https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/solutions/6512871/minimum-cost-walk-in-weighted-graph

type UnionFind struct {
	n    int
	root []int
	rank []int
}

func (uf *UnionFind) Init(n int) {
	uf.n = n
	uf.root = make([]int, n)
	for i := 0; i < n; i++ {
		uf.root[i] = i
	}
	uf.rank = make([]int, n)
}

func (uf *UnionFind) Find(x int) int {
	if uf.root[x] != x {
		uf.root[x] = uf.Find(uf.root[x])
	}
	return uf.root[x]
}

func (uf *UnionFind) Union(x, y int) {
	rx, ry := uf.Find(x), uf.Find(y)
	if rx == ry {
		return
	}
	if uf.rank[rx] < uf.rank[ry] {
		uf.root[rx] = ry
	} else if uf.rank[rx] > uf.rank[ry] {
		uf.root[ry] = rx
	} else {
		uf.root[rx] = ry
		uf.rank[ry]++
	}
}

func (uf *UnionFind) GetRoots() []int {
	for i := 0; i < uf.n; i++ {
		uf.Find(i)
	}
	root := map[int]bool{}
	for i := 0; i < uf.n; i++ {
		root[uf.root[i]] = true
	}
	// get keys
	keys := []int{}
	for k := range root {
		keys = append(keys, k)
	}
	return keys
}

func minimumCost(n int, edges [][]int, query [][]int) []int {
	uf := UnionFind{}
	uf.Init(n)
	for _, e := range edges {
		u, v := e[0], e[1]
		uf.Union(u, v)
	}
	componentCost := map[int]int{}

	for _, e := range edges {
		u, w := e[0], e[2]
		root := uf.Find(u)
		if v, ok := componentCost[root]; !ok {
			componentCost[root] = w
		} else {
			componentCost[root] = w & v
		}
	}

	ans := []int{}
	for _, q := range query {
		u, v := q[0], q[1]
		ru, rv := uf.Find(u), uf.Find(v)
		if ru != rv {
			ans = append(ans, -1)
			continue
		}
		ans = append(ans, componentCost[ru])
	}
	return ans
}

// @leet end

