/*
 * @lc app=leetcode id=208 lang=golang
 *
 * [208] Implement Trie (Prefix Tree)
 */

// @lc code=start
package main

var endSymbol rune = 'X'

type Trie struct {
	_t map[rune]Trie
}

func Constructor() Trie {
	t := make(map[rune]Trie)
	trie := Trie{_t: t}
	return trie
}

func (this *Trie) Insert(word string) {
	currTrie := *this
	for _, letter := range word {
		// insert letter to currTrie._t
		t, ok := currTrie._t[letter]
		if ok == false {
			newTrie := Constructor()
			currTrie._t[letter] = newTrie
			currTrie = newTrie
		} else {
			currTrie = t
		}
	}
	currTrie._t[endSymbol] = Constructor()
}

func (this *Trie) Search(word string) bool {
	currTrie := *this
	for _, letter := range word {
		innerTrie, ok := currTrie._t[letter]
		if ok == false {
			return false
		}
		currTrie = innerTrie
	}
	_, ok := currTrie._t[endSymbol]
	return ok
}

func (this *Trie) StartsWith(prefix string) bool {
	currTrie := *this
	for _, letter := range prefix {
		innerTrie, ok := currTrie._t[letter]
		if ok == false {
			return false
		}
		currTrie = innerTrie
	}
	return len(currTrie._t) > 0
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
// @lc code=end
