/*
 * @lc app=leetcode id=212 lang=golang
 *
 * [212] Word Search II
 */

// @lc code=start
/*
  use BFS with trie
  remember to remove the processed cell when BFS to avoid revisit (backtrack)
*/
package main

/* Trie impl */
var endSymbol rune = 'X'

type Trie struct {
	_t map[rune]*Trie
}

func getNewTrie() *Trie {
	t := make(map[rune]*Trie)
	trie := Trie{_t: t}
	return &trie
}

func (this *Trie) Insert(word string) {
	if len(word) == 0 {
		this._t[endSymbol] = getNewTrie()
		return
	}
	letter := rune(word[0])
	rest := word[1:]
	if inner, ok := this._t[letter]; !ok {
		newTrie := getNewTrie()
		this._t[letter] = newTrie
		newTrie.Insert(rest)
	} else {
		inner.Insert(rest)
	}
}

type DfsUnit struct {
	x int
	y int
	t *Trie
}

var d [][]int = [][]int{
	[]int{0, 1},
	[]int{1, 0},
	[]int{-1, 0},
	[]int{0, -1},
}

func findWords(board [][]byte, words []string) []string {
	trie := getNewTrie()
	for _, w := range words {
		trie.Insert(w)
	}
	ans := []string{}
	wordMap := make(map[string]bool) // ans hashmap
	m := len(board)
	n := len(board[0])

	var dfs func(u DfsUnit, pastLetters string)
	dfs = func(u DfsUnit, pastLetters string) {
		letter := board[u.x][u.y]
		char := rune(letter)
		nextTrie, ok := u.t._t[char]
		if !ok {
			return
		}
		if _, ok := nextTrie._t[endSymbol]; ok {
			s := pastLetters + string(letter)
			if _, ok := wordMap[s]; !ok {
				ans = append(ans, s)
				wordMap[s] = true
			}
		}
		board[u.x][u.y] = '-' // masking
		for _, dxdy := range d {
			dx, dy := dxdy[0], dxdy[1]
			nx := u.x + dx
			ny := u.y + dy
			if 0 <= nx && nx < m && 0 <= ny && ny < n {
				nextU := DfsUnit{nx, ny, nextTrie}
				nextPastLetters := pastLetters + string(letter)
				dfs(nextU, nextPastLetters)
			}
		}
		board[u.x][u.y] = letter // recover
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			// DFS
			unit := DfsUnit{i, j, trie}
			dfs(unit, "")
		}
	}
	// remove duplicate
	return ans
}

// @lc code=end
