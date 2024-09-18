/*
 * @lc app=leetcode id=211 lang=golang
 *
 * [211] Design Add and Search Words Data Structure
 */

// @lc code=start
package main

type WordDictionary struct {
	t map[rune]*WordDictionary
}

func Constructor() WordDictionary {
	trie := make(map[rune]*WordDictionary)
	return WordDictionary{
		t: trie,
	}
}

func getNewDict() *WordDictionary {
	trie := make(map[rune]*WordDictionary)
	return &WordDictionary{
		t: trie,
	}
}

func (this *WordDictionary) AddWord(word string) {
	n := len(word)
	if n == 0 {
		this.t['/'] = getNewDict()
		return
	}
	firstLetter := word[0]
	rest := word[1:]
	if _, ok := this.t[rune(firstLetter)]; !ok {
		this.t[rune(firstLetter)] = getNewDict()
	}
	this.t[rune(firstLetter)].AddWord(rest)
}

func (this *WordDictionary) Search(word string) bool {
	n := len(word)
	if n == 0 {
		_, ok := this.t['/']
		return ok
	}
	firstLetter := word[0]
	rest := word[1:]
	if firstLetter == '.' {
		// iterate all children in this.t
		// use OR and return the result
		for _, v := range this.t {
			if v.Search(rest) {
				return true
			}
		}
		return false
	}

	if _, ok := this.t[rune(firstLetter)]; !ok {
		return false
	}
	return this.t[rune(firstLetter)].Search(rest)
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */
// @lc code=end
