package main

// @leet start

// use Union-Find to solve the problem
// each disjoint set represent must be the lexicographically smallest character

type CharUnionFind struct {
	root []int
}

func getCharIndex(c byte) int {
	return int(c - 'a')
}

func indexToChar(index int) byte {
	return byte(index + 'a')
}

func (uf *CharUnionFind) init() {
	uf.root = make([]int, 26)
	for i := 0; i < 26; i++ {
		uf.root[i] = i
	}
}

func (uf *CharUnionFind) find(x int) int {
	if uf.root[x] != x {
		uf.root[x] = uf.find(uf.root[x])
	}
	return uf.root[x]
}

func (uf *CharUnionFind) union(x int, y int) {
	rx, ry := uf.find(x), uf.find(y)
	if rx == ry {
		return
	}
	// first compare lexicographical order
	if rx < ry {
		uf.root[ry] = rx
	} else {
		uf.root[rx] = ry
	}
}

func smallestEquivalentString(s1 string, s2 string, baseStr string) string {
	uf := &CharUnionFind{}
	uf.init()
	n := len(s1)
	for i := 0; i < n; i++ {
		b1 := s1[i]
		b2 := s2[i]
		c1 := getCharIndex(b1)
		c2 := getCharIndex(b2)
		uf.union(c1, c2)
	}
	ans := ""
	for _, c := range baseStr {
		b := byte(c)
		root := uf.find(getCharIndex(b))
		ans += string(indexToChar(root))
	}
	return ans
}

// n is the length of s1 and s2,
// m is the number of the items in disjoint sets, which is 26
// k is the length of baseStr
// O(nlgm + klgm)
// since m is a const, then the TC is O(n+k)

// @leet end
