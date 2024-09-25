/*
 * @lc app=leetcode id=2416 lang=golang
 *
 * [2416] Sum of Prefix Scores of Strings
 */

// @lc code=start
package main

/*
Trie
*/
type CountingTrie struct {
	t   map[rune]*CountingTrie
	num int
}

func getNewCountingTrie() *CountingTrie {
	trie := make(map[rune]*CountingTrie)
	n := 0
	return &CountingTrie{
		t:   trie,
		num: n,
	}
}

func (this *CountingTrie) AddWord(word string) {
	n := len(word)
	if n == 0 {
		_, ok := this.t['/']
		if !ok {
			this.t['/'] = getNewCountingTrie()
		}
		this.t['/'].num++
		return
	}
	firstLetter := word[0]
	rest := word[1:]
	if _, ok := this.t[rune(firstLetter)]; !ok {
		this.t[rune(firstLetter)] = getNewCountingTrie()
	}
	this.t[rune(firstLetter)].num++
	this.t[rune(firstLetter)].AddWord(rest)
}

func sumPrefixScores(words []string) []int {
	root := getNewCountingTrie()
	for _, w := range words {
		root.AddWord(w)
	}
	// cache := make(map[string]int)
	ans := []int{}

	for _, w := range words {
		n := len(w)
		res := 0 // sum of score for this word w
		idx := 0
		currTrie := root
		for idx < n {
			innerTrie, ok := currTrie.t[rune(w[idx])]
			if !ok {
				break
			}
			res += innerTrie.num
			idx++
			currTrie = innerTrie
		}
		ans = append(ans, res)
	}
	return ans
}

// @lc code=end
