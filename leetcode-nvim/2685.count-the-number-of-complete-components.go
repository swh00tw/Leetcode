package main

// @leet start
// 1. BFS
// 2. UnionFind

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

func countCompleteComponents(n int, edges [][]int) int {
	uf := &UnionFind{}
	uf.Init(n)
	for _, e := range edges {
		uf.Union(e[0], e[1])
	}

	// for each connected components, there must be n*(n-1)/2 edges
	nodes := make(map[int]int)
	for i := 0; i < n; i++ {
		nodes[uf.Find(i)]++
	}
	roots := make(map[int]int)
	for _, e := range edges {
		key := uf.Find(e[0])
		roots[key]++
	}

	ans := 0
	for k, v := range nodes {
		if v == 1 {
			if roots[k] == 0 {
				ans++
			}
		} else if v > 1 {
			if roots[k] == v*(v-1)/2 {
				ans++
			}
		}
	}

	return ans
}

// @leet end

