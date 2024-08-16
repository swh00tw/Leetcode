/*
 * @lc app=leetcode id=2462 lang=golang
 *
 * [2462] Total Cost to Hire K Workers
 */

// @lc code=start
package main

import "container/heap"

func totalCost(costs []int, k int, candidates int) int64 {
	lBound, rBound := candidates-1, len(costs)-candidates
	h := &Heap{}
	cost := 0
	for i := 0; i <= lBound; i++ {
		heap.Push(h, []int{costs[i], i})
	}
	for i := len(costs) - 1; i >= rBound && i > lBound; i-- {
		heap.Push(h, []int{costs[i], i})
	}
	// lBound, rBound already pushed
	for k > 0 && h.Len() > 0 {
		k--
		v := heap.Pop(h).([]int)
		cost += v[0]
		if rBound-lBound > 1 {
			if v[1] <= lBound {
				lBound++
				heap.Push(h, []int{costs[lBound], lBound})
			} else {
				rBound--
				heap.Push(h, []int{costs[rBound], rBound})
			}
		}
	}
	return int64(cost)
}

type Heap [][]int

func (p *Heap) Len() int { return len(*p) }
func (p *Heap) Less(i, j int) bool {
	if (*p)[i][0] == (*p)[j][0] {
		return (*p)[i][1] < (*p)[j][1]
	}
	return (*p)[i][0] < (*p)[j][0]
}
func (p *Heap) Swap(i, j int) {
	(*p)[i], (*p)[j] = (*p)[j], (*p)[i]
}
func (p *Heap) Push(i interface{}) {
	*p = append(*p, i.([]int))
}
func (p *Heap) Pop() interface{} {
	v := (*p)[len(*p)-1]
	*p = (*p)[:len(*p)-1]
	return v
}

// @lc code=end
