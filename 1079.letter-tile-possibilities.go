/*
 * @lc app=leetcode id=1079 lang=golang
 *
 * [1079] Letter Tile Possibilities
 */

// @lc code=start
package main

/*
  use trie
*/

var endSymbol rune = 'X'

type Trie struct {
	_t map[rune]Trie
}

func Constructor() Trie {
	t := make(map[rune]Trie)
	trie := Trie{_t: t}
	return trie
}

func (this *Trie) Insert(word string) int {
	if len(word) == 0 {
		this._t[endSymbol] = Constructor()
		return 0
	}
	letter := rune(word[0])
	rest := word[1:]
	if inner, ok := this._t[letter]; !ok {
		newTrie := Constructor()
		this._t[letter] = newTrie
		return 1 + newTrie.Insert(rest)
	} else {
		return inner.Insert(rest)
	}
}

func numTilePossibilities(tiles string) int {
	freq := make(map[rune]int)
	for _, c := range tiles {
		freq[c]++
	}
	allPermutations := getAllPermutations(freq)

	ans := 0
	trie := Constructor()
	for _, p := range allPermutations {
		ans += trie.Insert(p)
	}
	return ans
}

func getAllPermutations(freq map[rune]int) []string {
	ans := []string{}
	for k, v := range freq {
		if v == 0 {
			continue
		}
		freq[k]--
		substrings := getAllPermutations(freq)
		for _, s := range substrings {
			ans = append(ans, string(k)+s)
		}
		freq[k]++
	}
	if len(ans) == 0 {
		return []string{""}
	}
	return ans
}

// @lc code=end
