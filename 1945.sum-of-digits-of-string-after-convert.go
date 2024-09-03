/*
 * @lc app=leetcode id=1945 lang=golang
 *
 * [1945] Sum of Digits of String After Convert
 */

// @lc code=start
package main

import (
	"strconv"
)

func letter2String(s rune) string {
	n := int(s) - 'a' + 1
	return strconv.Itoa(n)
}

func ops(numberString string) int {
	s := 0
	for i := 0; i < len(numberString); i++ {
		c := string(numberString[i])
		n, _ := strconv.Atoi(c)
		s += n
	}
	return s
}

func int2Str(n int) string {
	return strconv.Itoa(n)
}

func getLucky(s string, k int) int {
	// first turn the s to number string
	// run operation k times
	// transform string to int
	str := ""
	for _, b := range s {
		str += letter2String(b)
	}
	for i := 0; i < k; i++ {
		nextInt := ops(str)
		str = int2Str(nextInt)
	}
	n, _ := strconv.Atoi(str)
	return n
}

// @lc code=end
