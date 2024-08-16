/*
 * @lc app=leetcode id=739 lang=golang
 *
 * [739] Daily Temperatures
 */

// @lc code=start
package main

func dailyTemperatures(temperatures []int) []int {
	/*
	   Maintain a stack, store [val, idx]
	   Only decreasing,
	   iterate thru the arr, when the temp higher than top of the stack
	   keep popping, and update ans array
	*/
	stack := [][]int{}
	n := len(temperatures)
	ans := make([]int, n)
	for i, temp := range temperatures {
		for len(stack) > 0 && stack[len(stack)-1][0] < temp {
			idx := stack[len(stack)-1][1]
			ans[idx] = i - idx
			// pop
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, []int{temp, i})
	}
	return ans
}

// @lc code=end
