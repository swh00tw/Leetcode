/*
 * @lc app=leetcode id=731 lang=golang
 *
 * [731] My Calendar II
 */

// @lc code=start
package main

type MyCalendarTwo struct {
	one [][]int // segments of one book
	two [][]int // segments of dobule books
}

func Constructor() MyCalendarTwo {
	return MyCalendarTwo{[][]int{}, [][]int{}}
}

// return intersection part
func inter(x0, x1, y0, y1 int) []int {
	if x0 > y0 {
		x0, y0 = y0, x0
		x1, y1 = y1, x1
	}
	if y0 >= x1 {
		return []int{}
	}
	if y0 <= x0 && y1 > x1 {
		return []int{x0, x1}
	}
	if x0 <= y0 && x1 > y1 {
		return []int{y0, y1}
	}
	return []int{y0, x1}
}

func (this *MyCalendarTwo) Book(l int, r int) bool {
	for _, x := range this.two {
		z := inter(x[0], x[1], l, r)
		// has intersection
		if len(z) > 0 {
			return false
		}
	}
	for _, x := range this.one {
		z := inter(x[0], x[1], l, r)
		if len(z) > 0 {
			this.two = append(this.two, z)
		}
	}
	this.one = append(this.one, []int{l, r})
	return true
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
// @lc code=end
