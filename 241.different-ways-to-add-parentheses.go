/*
 * @lc app=leetcode id=241 lang=golang
 *
 * [241] Different Ways to Add Parentheses
 */

// @lc code=start
package main

import "strconv"

/*
  recursive divide the problem
  base case, only one number in the expression, no operators
  other cases, we can split problem at each operator
  ex: '2*3-4' -> 2*(3-4), (2*3)-4
*/

func diffWaysToCompute(expression string) []int {
	hasOperators := false
	for _, c := range expression {
		if c == '*' || c == '+' || c == '-' {
			hasOperators = true
		}
	}
	ans := []int{}
	if !hasOperators {
		val, _ := strconv.Atoi(expression)
		ans = append(ans, val)
		return ans
	}
	// general case
	for i, c := range expression {
		if c == '*' {
			leftAns := diffWaysToCompute(expression[:i])
			rightAns := diffWaysToCompute(expression[i+1:])
			for _, l := range leftAns {
				for _, r := range rightAns {
					ans = append(ans, l*r)
				}
			}
		}
		if c == '+' {
			leftAns := diffWaysToCompute(expression[:i])
			rightAns := diffWaysToCompute(expression[i+1:])
			for _, l := range leftAns {
				for _, r := range rightAns {
					ans = append(ans, l+r)
				}
			}
		}
		if c == '-' {
			leftAns := diffWaysToCompute(expression[:i])
			rightAns := diffWaysToCompute(expression[i+1:])
			for _, l := range leftAns {
				for _, r := range rightAns {
					ans = append(ans, l-r)
				}
			}
		}
	}
	return ans
}

// @lc code=end
