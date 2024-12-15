/*
 * @lc app=leetcode id=1792 lang=golang
 *
 * [1792] Maximum Average Pass Ratio
 */

// @lc code=start
package main

import "container/heap"

// use heap
// sort by "how much value of ratio can be increased if assigning a new passed student" (let's call it potential)

type Class struct {
	pass  int
	total int
}

func (c *Class) GetPotential() float64 {
	return float64(c.pass+1)/float64(c.total+1) - float64(c.pass)/float64(c.total)
}

func (c *Class) GetRatio() float64 {
	return float64(c.pass) / float64(c.total)
}

type ClassHeap []Class

func (p *ClassHeap) Len() int { return len(*p) }
func (p *ClassHeap) Less(i, j int) bool {
	return (*p)[i].GetPotential() > (*p)[j].GetPotential() // reverse to turn min heap into max heap
}
func (p *ClassHeap) Swap(i, j int) {
	(*p)[i], (*p)[j] = (*p)[j], (*p)[i]
}
func (p *ClassHeap) Push(i interface{}) {
	*p = append(*p, i.(Class))
}
func (p *ClassHeap) Pop() interface{} {
	v := (*p)[len(*p)-1]
	*p = (*p)[:len(*p)-1]
	return v
}

func maxAverageRatio(classes [][]int, extraStudents int) float64 {
	n := float64(len(classes))
	classesHeap := &ClassHeap{}
	for _, c := range classes {
		heap.Push(classesHeap, Class{
			pass:  c[0],
			total: c[1],
		})
	}
	for i := 0; i < extraStudents; i++ {
		// pop class with the highest potential
		class := heap.Pop(classesHeap).(Class)
		heap.Push(classesHeap, Class{
			pass:  class.pass + 1,
			total: class.total + 1,
		})
	}
	total := float64(0)
	for classesHeap.Len() > 0 {
		class := heap.Pop(classesHeap).(Class)
		total += class.GetRatio()
	}
	return total / n
}

// @lc code=end
