/*
 * @lc app=leetcode id=1514 lang=golang
 *
 * [1514] Path with Maximum Probability
 */

// @lc code=start
package main

import "container/heap"

/*
  Shortest path problem: Dijkstra
  1. need a heap to store current priority queue (maxHeap)
  2. first push the source to pq
  3. keep popping, and do relaxation (and push to pq)

  TC: O(ElogV) (Time complexity for dijkstra)
  SC: O(V^2) (bcz adjList)
*/

type HeapItem struct {
	val float64
	idx int
}

type Heap []HeapItem

func (pq *Heap) Len() int {
	return len(*pq)
}

func (pq *Heap) Less(i, j int) bool {
	return (*pq)[i].val < (*pq)[j].val
}

func (pq *Heap) Swap(i, j int) {
	(*pq)[i], (*pq)[j] = (*pq)[j], (*pq)[i]
}

func (pq *Heap) Push(i any) {
	*pq = append(*pq, i.(HeapItem))
}

func (pq *Heap) Pop() any {
	l := len(*pq)
	v := (*pq)[l-1]
	*pq = (*pq)[:l-1]
	return v
}

type AdjListEntry struct {
	prob float64
	src  int
	dst  int
}

func maxProbability(n int, edges [][]int, succProb []float64, start int, end int) float64 {
	// build adjList
	adjList := make(map[int][]AdjListEntry)
	for i := 0; i < len(succProb); i++ {
		prob := succProb[i]
		e := edges[i]
		src := e[0]
		dst := e[1]
		if _, okSrc := adjList[src]; !okSrc {
			adjList[src] = make([]AdjListEntry, 0)
		}
		adjList[src] = append(adjList[src], AdjListEntry{
			prob: prob,
			src:  src,
			dst:  dst,
		})
		if _, okDst := adjList[dst]; !okDst {
			adjList[dst] = make([]AdjListEntry, 0)
		}
		adjList[dst] = append(adjList[dst], AdjListEntry{
			prob: prob,
			src:  dst,
			dst:  src,
		})
	}
	// dijkstra
	distance := make([]float64, n)
	distance[start] = 1.0
	pq := &Heap{}
	heap.Push(pq, HeapItem{
		val: -1.0,
		idx: start,
	})
	for pq.Len() > 0 {
		node := heap.Pop(pq).(HeapItem)
		p := -node.val
		if node.idx == end {
			return p
		}
		// relaxation for each neighbor
		for _, neighbor := range adjList[node.idx] {
			if p*neighbor.prob > distance[neighbor.dst] {
				distance[neighbor.dst] = p * neighbor.prob
				heap.Push(pq, HeapItem{
					val: -p * neighbor.prob,
					idx: neighbor.dst,
				})
			}
		}
	}
	return 0
}

// @lc code=end
