/*
 * @lc app=leetcode id=641 lang=golang
 *
 * [641] Design Circular Deque
 */

// @lc code=start
package main

type Deque[T any] struct {
	elems    []T
	currSize int
	maxSize  int
}

type MyCircularDeque Deque[int]

func Constructor(k int) MyCircularDeque {
	return MyCircularDeque{
		elems:    []int{},
		currSize: 0,
		maxSize:  k,
	}
}

func (this *MyCircularDeque) InsertFront(value int) bool {
	if this.IsFull() {
		return false
	}
	this.currSize++
	newElems := append([]int{value}, this.elems...)
	this.elems = newElems
	return true
}

func (this *MyCircularDeque) InsertLast(value int) bool {
	if this.IsFull() {
		return false
	}
	this.currSize++
	this.elems = append(this.elems, value)
	return true
}

func (this *MyCircularDeque) DeleteFront() bool {
	if this.IsEmpty() {
		return false
	}
	this.currSize--
	this.elems = this.elems[1:]
	return true
}

func (this *MyCircularDeque) DeleteLast() bool {
	if this.IsEmpty() {
		return false
	}
	this.currSize--
	this.elems = this.elems[:this.currSize]
	return true
}

func (this *MyCircularDeque) GetFront() int {
	if this.IsEmpty() {
		return -1
	}
	return this.elems[0]
}

func (this *MyCircularDeque) GetRear() int {
	if this.IsEmpty() {
		return -1
	}
	return this.elems[this.currSize-1]
}

func (this *MyCircularDeque) IsEmpty() bool {
	return this.currSize == 0
}

func (this *MyCircularDeque) IsFull() bool {
	return this.currSize == this.maxSize
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.InsertFront(value);
 * param_2 := obj.InsertLast(value);
 * param_3 := obj.DeleteFront();
 * param_4 := obj.DeleteLast();
 * param_5 := obj.GetFront();
 * param_6 := obj.GetRear();
 * param_7 := obj.IsEmpty();
 * param_8 := obj.IsFull();
 */
// @lc code=end
