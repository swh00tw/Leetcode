package main

import (
	"container/heap"
	"math"
)

// @leet start

// Dijikstra shortest path algorithm
// use a priority queue to find the minimum time to reach the last room

var MAX_INT = math.MaxInt

type Node struct {
	x, y        int
	timeToReact int
}
type PriorityQueue []Node

// heap impl
func (pq *PriorityQueue) Len() int {
	return len(*pq)
}

func (pq *PriorityQueue) Less(i, j int) bool {
	return (*pq)[i].timeToReact < (*pq)[j].timeToReact
}

func (pq *PriorityQueue) Swap(i, j int) {
	(*pq)[i], (*pq)[j] = (*pq)[j], (*pq)[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
	(*pq) = append(*pq, x.(Node))
}

func (pq *PriorityQueue) Pop() interface{} {
	node := (*pq)[len(*pq)-1]
	(*pq) = (*pq)[:len(*pq)-1]
	return node
}

var deltas = [][]int{
	{0, 1},
	{1, 0},
	{0, -1},
	{-1, 0},
}

func minTimeToReach(moveTime [][]int) int {
	n := len(moveTime)
	m := len(moveTime[0])
	time := make([][]int, n)
	for i := 0; i < n; i++ {
		time[i] = make([]int, m)
		for j := 0; j < m; j++ {
			time[i][j] = MAX_INT
		}
	}
	time[0][0] = 0

	nodes := make(PriorityQueue, 0)
	nodes = append(nodes, Node{0, 0, 0})
	for len(nodes) > 0 {
		node := heap.Pop(&nodes).(Node)
		currentTime := node.timeToReact
		// relaxation to adjacent nodes
		for _, delta := range deltas {
			nx := node.x + delta[0]
			ny := node.y + delta[1]
			if nx >= 0 && nx < n && ny >= 0 && ny < m {
				newTimeToReact := currentTime
				if moveTime[nx][ny] > currentTime {
					newTimeToReact = moveTime[nx][ny]
				}
				newTimeToReact++
				if newTimeToReact < time[nx][ny] {
					time[nx][ny] = newTimeToReact
					heap.Push(&nodes, Node{nx, ny, newTimeToReact})
				}
			}
		}
	}
	return time[n-1][m-1]
}

// @leet end

