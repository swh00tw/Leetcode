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
	if len(word) == 0 {
		this._t[endSymbol] = Constructor()
		return
	}
	letter := rune(word[0])
	rest := word[1:]
	if inner, ok := this._t[letter]; !ok {
		newTrie := Constructor()
		this._t[letter] = newTrie
		newTrie.Insert(rest)
	} else {
		inner.Insert(rest)
	}
}

func (this *Trie) Search(word string) bool {
	if len(word) == 0 {
		_, ok := this._t[endSymbol]
		return ok
	}
	letter := rune(word[0])
	rest := word[1:]
	innerTrie, ok := this._t[letter]
	if !ok {
		return false
	}
	return innerTrie.Search(rest)

}

func (this *Trie) StartsWith(prefix string) bool {
	if len(prefix) == 0 {
		return len(this._t) > 0
	}
	letter := rune(prefix[0])
	rest := prefix[1:]
	innerTrie, ok := this._t[letter]
	if !ok {
		return false
	}
	return innerTrie.StartsWith(rest)
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
// @lc code=end
