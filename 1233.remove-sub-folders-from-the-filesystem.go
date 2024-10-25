/*
 * @lc app=leetcode id=1233 lang=golang
 *
 * [1233] Remove Sub-Folders from the Filesystem
 */

// @lc code=start
package main

import (
	"fmt"
	"sort"
	"strings"
)

/*Trie*/

type Trie struct {
	next   map[string]*Trie
	hasEnd bool
}

func newTrie() *Trie {
	t := Trie{
		next:   make(map[string]*Trie),
		hasEnd: false,
	}
	return &t
}

func (t *Trie) Print() {
	fmt.Println(t)
	for k, v := range t.next {
		fmt.Println(k)
		v.Print()
	}
}

func (t *Trie) Insert(folders []string) {
	if len(folders) == 0 {
		t.hasEnd = true
		return
	}
	first := folders[0]
	rest := folders[1:]
	if _, ok := t.next[first]; !ok {
		t.next[first] = newTrie()
	}
	t.next[first].Insert(rest)
}

// return true if there's any hasEnd along the path
func (t *Trie) Search(folders []string) bool {
	if t.hasEnd {
		return true
	}
	first := folders[0]
	rest := folders[1:]
	if _, ok := t.next[first]; !ok {
		return false
	}
	return t.next[first].Search(rest)
}

func removeSubfolders(folder []string) []string {
	root := newTrie()
	ans := make([]string, 0)

	fs := make([][]string, 0)
	for _, f := range folder {
		ff := strings.Split(f[1:], "/")
		fs = append(fs, ff)
	}
	sort.Slice(fs, func(i, j int) bool {
		return len(fs[i]) < len(fs[j])
	})

	// sort based on the length of item
	// if not in other folder, insert to ans
	// insert this path to root in the end
	for _, f := range fs {
		inOtherFolder := root.Search(f)
		if !inOtherFolder {
			ans = append(ans, "/"+strings.Join(f, "/"))
		}
		root.Insert(f)
	}
	return ans
}

// @lc code=end
