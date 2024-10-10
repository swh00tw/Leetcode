/*
 * @lc app=leetcode id=962 lang=golang
 *
 * [962] Maximum Width Ramp
 */

// @lc code=start
package main

func maxWidthRamp(nums []int) int {
	/*
	   maintain a stack (monotonic decreasing)
	   they are potential left bound
	   O(n) here
	   From right to left, find potential right bound,
	   if the num is larger than stack top, pop stack pop and keep finding left bound
	   O(n)
	*/
	stack := make([][]int, 0) // [val, idx]
	bestAns := 0
	for idx, num := range nums {
		if idx == 0 {
			stack = append(stack, []int{num, idx})
			continue
		}
		if num < stack[len(stack)-1][0] {
			stack = append(stack, []int{num, idx})
		}
	}
	for i := len(nums) - 1; i >= 0; i-- {
		for len(stack) > 0 && stack[len(stack)-1][0] <= nums[i] {
			// update bestAns, and pop item
			potentialAns := i - stack[len(stack)-1][1]
			if potentialAns >= bestAns {
				bestAns = potentialAns
			}
			// pop
			stack = stack[:len(stack)-1]
		}
	}

	return bestAns
}

// @lc code=end
