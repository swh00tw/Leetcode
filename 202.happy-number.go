/*
 * @lc app=leetcode id=202 lang=golang
 *
 * [202] Happy Number
 */

// @lc code=start
package main

func isHappy(n int) bool {
	if n == 1 {
		return true
	}
	cache := make(map[int]int)

	var findHappy func(n int) bool
	findHappy = func(n int) bool {
		if n == 1 {
			return true
		}
		num := n
		nextNum := 0
		for num > 0 {
			lastDigit := num % 10
			num /= 10
			nextNum += lastDigit * lastDigit
		}
		if nextNum == 1 {
			return true
		}
		if _, ok := cache[nextNum]; ok {
			// find cycle
			return false
		} else {
			cache[nextNum] = 1
		}
		return findHappy(nextNum)
	}
	return findHappy(n)
}

// @lc code=end
