package main

import (
	"container/heap"
	"math"
)

// @leet start
type HeapItem struct {
	time int
	node int
}
type Heap []HeapItem

func (pq *Heap) Len() int { return len(*pq) }
func (pq *Heap) Less(i, j int) bool {
	return (*pq)[i].time < (*pq)[j].time
}

func (pq *Heap) Swap(i, j int) {
	(*pq)[i], (*pq)[j] = (*pq)[j], (*pq)[i]
}

func (pq *Heap) Push(x interface{}) {
	(*pq) = append(*pq, x.(HeapItem))
}

func (pq *Heap) Pop() interface{} {
	x := (*pq)[len(*pq)-1]
	(*pq) = (*pq)[:len(*pq)-1]
	return x
}

func countPaths(n int, roads [][]int) int {
	adjList := make(map[int][][]int)
	for i := 0; i < n; i++ {
		adjList[i] = make([][]int, 0)
	}
	for _, r := range roads {
		src, dst, time := r[0], r[1], r[2]
		adjList[src] = append(adjList[src], []int{dst, time})
		adjList[dst] = append(adjList[dst], []int{src, time})
	}
	// Dijkstra, use two array: time and ways to store states
	time := make([]int, n)
	for i := 0; i < n; i++ {
		time[i] = math.MaxInt
	}
	ways := make([]int, n)

	ways[0] = 1
	time[0] = 0
	pq := &Heap{}
	heap.Push(pq, HeapItem{0, 0})
	for len(*pq) > 0 {
		// pop
		item := heap.Pop(pq).(HeapItem)
		// outdated
		if item.time > time[item.node] {
			continue
		}

		for _, neighborTimePair := range adjList[item.node] {
			nei, t := neighborTimePair[0], neighborTimePair[1]
			if item.time+t < time[nei] {
				time[nei] = time[item.node] + t
				ways[nei] = ways[item.node]
				heap.Push(pq, HeapItem{time[nei], nei})
			} else if item.time+t == time[nei] {
				ways[nei] = (ways[nei] + ways[item.node]) % 1000000007
			}
		}
	}

	return ways[n-1]
}

// @leet end
