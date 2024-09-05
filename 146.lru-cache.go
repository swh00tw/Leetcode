/*
 * @lc app=leetcode id=146 lang=golang
 *
 * [146] LRU Cache
 */

// @lc code=start
package main

type Node struct {
	prev *Node
	next *Node
	key  int
	val  int
}

type LRUCache struct {
	len    int
	llhead *Node // double linked list
	cache  map[int]*Node
	cap    int
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		len:    0,
		llhead: nil,
		cache:  make(map[int]*Node),
		cap:    capacity,
	}
}

func (this *LRUCache) MoveToHead(node *Node) {
	if this.len == 0 {
		panic("SHOULD NEVER HAPPEN")
	}
	// edge case 1: node is head
	if this.llhead == node {
		return
	}
	// edge case 2: node is tail
	if this.llhead.prev == node {
		this.llhead = node
		return
	}
	// link prev and next
	prev := node.prev
	next := node.next
	prev.next = next
	next.prev = prev
	// move node to head
	tail := this.llhead.prev
	node.prev = tail
	node.next = this.llhead
	tail.next = node
	this.llhead.prev = node
	this.llhead = node
}

func (this *LRUCache) AppendToHead(node *Node) {
	this.len++
	// update cache
	this.cache[node.key] = node
	if this.llhead == nil {
		node.prev = node
		node.next = node
		this.llhead = node
		return
	}
	tail := this.llhead.prev
	// link node to front
	node.prev = tail
	node.next = this.llhead
	// update old head and tail
	this.llhead.prev = node
	tail.next = node
	this.llhead = node
}

func (this *LRUCache) RemoveTail() {
	this.len--
	// update cache
	delete(this.cache, this.llhead.prev.key)
	if this.len == 0 {
		this.llhead = nil
		return
	}
	tail := this.llhead.prev
	newTail := tail.prev
	newTail.next = this.llhead
	this.llhead.prev = newTail
}

func (this *LRUCache) Get(key int) int {
	if node, ok := this.cache[key]; ok {
		this.MoveToHead(node)
		return node.val
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	if node, ok := this.cache[key]; ok {
		node.val = value
		this.MoveToHead(node)
		return
	}
	if this.len == this.cap {
		this.RemoveTail()
	}
	newNode := &Node{
		key:  key,
		val:  value,
		prev: nil,
		next: nil,
	}
	this.AppendToHead(newNode)
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
// @lc code=end
