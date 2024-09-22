/*
 * @lc app=leetcode id=386 lang=golang
 *
 * [386] Lexicographical Numbers
 */

// @lc code=start
package main

// ref: https://leetcode.com/problems/lexicographical-numbers/solutions/5814144/explained-simple-and-easy-python-solution-o-n
func lexicalOrder(n int) []int {
	num := 1
	ans := []int{}
	for len(ans) < n {
		ans = append(ans, num)

		if num*10 <= n {
			num *= 10
		} else if num%10 != 9 && num+1 <= n {
			num++
		} else {
			for (num/10)%10 == 9 {
				num /= 10
			}
			num = (num / 10) + 1
		}
	}
	return ans
}

// @lc code=end
