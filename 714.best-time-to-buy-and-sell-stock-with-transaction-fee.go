/*
 * @lc app=leetcode id=714 lang=golang
 *
 * [714] Best Time to Buy and Sell Stock with Transaction Fee
 */

// @lc code=start
package main

import "math"

func maxProfit(prices []int, fee int) int {
	/* 1d dp problem
	# create two array, free & hold
	# free[i] represent the maximum profit can gain on the i-th day without holding stock
	# hold[i] represent the maximum profit can gain on the i-th day with stock holding
	# optimal substructure
	# free[i] = hold[i-1]+prices[i]-fee (selling on i-th day) OR free[i-1] (no sell on i-th day)
	# hold[i] = free[i-1]-prices[i] (buying on i-th day) OR hold[i-1] (no buy on i-th day)
	# base case:
	# free[0] = 0
	# hold[0] = -prices[0]
	*/
	n := len(prices)
	free := make([]int, n)
	hold := make([]int, n)
	free[0] = 0
	hold[0] = -prices[0]
	for i := 1; i < n; i++ {
		free[i] = intMax(free[i-1], hold[i-1]+prices[i]-fee)
		hold[i] = intMax(hold[i-1], free[i-1]-prices[i])
	}
	return free[n-1]
}

func intMax(x, y int) int {
	xf := float64(x)
	yf := float64(y)
	return int(math.Max(xf, yf))
}

// @lc code=end
