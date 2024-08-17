/*
 * @lc app=leetcode id=901 lang=golang
 *
 * [901] Online Stock Span
 */

// @lc code=start
package main

import "math"

/*
Maintain a monotonic stack [val, days] only decreasing order by val
*/
type StockSpanner struct {
	stack [][]int
}

func Constructor() StockSpanner {
	return StockSpanner{stack: [][]int{}}
}

func (this *StockSpanner) Next(price int) int {
	/*
	   1. keep compare from the top of the stack, to get the ans
	   2. merge this into the top element of the stack if needed
	*/
	ans := 1
	n := len(this.stack)
	for i := n - 1; i >= 0; i-- {
		elem := this.stack[i]
		if elem[0] <= price {
			ans += elem[1]
		} else {
			break
		}
	}
	if n == 0 {
		this.stack = append(this.stack, []int{price, 1})
	} else {
		top := this.stack[n-1]
		if price >= top[0] {
			this.stack[n-1][1]++
			this.stack[n-1][0] = max(this.stack[n-1][0], price)
		} else {
			this.stack = append(this.stack, []int{price, 1})
		}
	}
	return ans
}

func max(a, b int) int {
	return int(math.Max(float64(a), float64(b)))
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
// @lc code=end
