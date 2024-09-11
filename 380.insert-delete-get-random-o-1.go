/*
 * @lc app=leetcode id=380 lang=golang
 *
 * [380] Insert Delete GetRandom O(1)
 */

// @lc code=start
package main

/*
  use an array to store items in the arr
  use a hashmap to map the item to the index in array
*/
import (
	"math/rand"
)

type RandomizedSet struct {
	items   []int // only insertion
	key2idx map[int]int
	deleted map[int]bool
}

func Constructor() RandomizedSet {
	return RandomizedSet{
		items:   []int{},
		key2idx: make(map[int]int),
		deleted: make(map[int]bool),
	}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.key2idx[val]; ok {
		return false
	}
	this.items = append(this.items, val)
	this.key2idx[val] = len(this.items) - 1
	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	if _, ok := this.key2idx[val]; !ok {
		return false
	}
	// remove key val from key2Idx
	idx := this.key2idx[val]
	delete(this.key2idx, val)
	// update deleted
	this.deleted[idx] = true
	return true
}

func (this *RandomizedSet) GetRandom() int {
	// get random idx from 1 to len(this.items)-1
	// if that's not deleted, return
	// if that's deleted, move to right one or redo randomize pick again
	idx := getRandomIdx(len(this.items))
	if _, ok := this.deleted[idx]; !ok {
		return this.items[idx]
	}
	for {
		i := getRandomIdx(len(this.items))
		if _, ok := this.deleted[i]; !ok {
			return this.items[i]
		}
	}
}

func getRandomIdx(n int) int {
	return rand.Intn(n)
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
// @lc code=end
