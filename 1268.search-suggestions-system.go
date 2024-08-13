/*
 * @lc app=leetcode id=1268 lang=golang
 *
 * [1268] Search Suggestions System
 */

// @lc code=start
package main

import (
	"sort"
)

func insertString(ss []string, s string) []string {
	// Find the index where the string should be inserted
	i := sort.SearchStrings(ss, s)
	// Append a zero value to the slice to make room for the new string
	ss = append(ss, "")
	// Shift the elements to the right to create space for the new string
	copy(ss[i+1:], ss[i:])
	// Insert the new string at the found index
	ss[i] = s
	return ss
}

type Trie struct {
	_t       map[rune]*Trie // Change to pointer to Trie
	products []string
}

func newTrie() *Trie { // Return a pointer to Trie
	return &Trie{_t: make(map[rune]*Trie), products: []string{}}
}

func (this *Trie) Insert(val string) {
	currTrie := this // Use the pointer directly
	for _, letter := range val {
		if inner, ok := currTrie._t[letter]; ok == false {
			newTrie := newTrie()
			currTrie._t[letter] = newTrie
			currTrie = newTrie
		} else {
			currTrie = inner
		}
		// Append the product to the current node's products
		currTrie.products = insertString(currTrie.products, val)
	}
}

func suggestedProducts(products []string, searchWord string) [][]string {
	// 1. build a trie
	trie := newTrie()
	for _, product := range products {
		trie.Insert(product)
	}
	n := len(searchWord)
	res := make([][]string, n)
	for i := 0; i < n; i++ {
		res[i] = []string{}
	}
	currTrie := trie
	for i, letter := range searchWord {
		innerTrie, ok := currTrie._t[letter]
		if !ok {
			break
		}
		if len(innerTrie.products) >= 3 {
			res[i] = innerTrie.products[:3]
		} else {
			res[i] = innerTrie.products
		}
		currTrie = innerTrie // Move to the next node
	}
	return res
}

// @lc code=end
