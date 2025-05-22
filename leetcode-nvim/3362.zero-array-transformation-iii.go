package main

import "container/heap"

// @leet start
// sol: https://leetcode.com/problems/zero-array-transformation-iii/solutions/6768363/python-solution-explained
func maxRemoval(nums []int, queries [][]int) int {
	n, q := len(nums), len(queries)
	starts := make([][]int, n)
	for _, qr := range queries {
		starts[qr[0]] = append(starts[qr[0]], qr[1])
	}

	avail := &MaxHeap{}
	heap.Init(avail)

	expireAt := make([]int, n)
	chosen, expired := 0, 0

	for i := 0; i < n; i++ {
		// add newly starting intervals
		for _, r := range starts[i] {
			heap.Push(avail, r)
		}
		// expire intervals that ended at i-1
		if i > 0 {
			expired += expireAt[i-1]
		}
		active := chosen - expired
		need := nums[i] - active
		for need > 0 {
			// drop any that can't cover i
			for avail.Len() > 0 && (*avail)[0] < i {
				heap.Pop(avail)
			}
			if avail.Len() == 0 {
				return -1
			}
			r := heap.Pop(avail).(int)
			expireAt[r]++
			chosen++
			need--
		}
	}
	return q - chosen
}

type MaxHeap []int

func (h MaxHeap) Len() int            { return len(h) }
func (h MaxHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h MaxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// @leet end

