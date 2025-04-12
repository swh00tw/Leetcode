package main

import (
	"fmt"
	"slices"
	"strconv"
)

// @leet start

/*
* Combine the solution here: https://leetcode.com/problems/find-the-count-of-good-integers/solutions/6622407/find-the-count-of-good-integers
* And my own solution.
* For how to iterate thru all palinfrome for given number of digits, see the link
* */
func countGoodIntegers(n int, k int) int64 {
	count := int64(0)

	// to avoid checking numbers with the same key
	keys := make(map[string]bool)
	getNumKey := func(n int) string {
		digits := []int{}
		for n > 0 {
			digit := n % 10
			digits = append(digits, digit)
			n /= 10
		}
		slices.Sort(digits)
		key := ""
		for _, digit := range digits {
			key += fmt.Sprintf("%d", digit)
		}
		return key
	}

	factorial := make(map[int]int64)
	getFactorial := func(n int) int64 {
		if v, ok := factorial[n]; ok {
			return v
		}
		num := int64(1)
		for i := 1; i <= n; i++ {
			num *= int64(i)
		}
		factorial[n] = num
		return num
	}
	nFactorial := getFactorial(n)
	nMinusOneFactorial := getFactorial(n - 1)

	countCombination := func(n int) int64 {
		digits := make(map[int]int)
		for n > 0 {
			digit := n % 10
			digits[digit]++
			n /= 10
		}

		// count combination
		totalComb := nFactorial
		for _, v := range digits {
			totalComb /= getFactorial(v)
		}
		// get the number of comb which is lead by zero
		if _, ok := digits[0]; !ok {
			return totalComb
		}
		digits[0]--
		ledByZero := nMinusOneFactorial
		for _, v := range digits {
			ledByZero /= getFactorial(v)
		}
		return totalComb - ledByZero
	}

	base := intPow(10, (n-1)/2)
	skip := n & 1
	/* Enumerate the number of palindrome numbers of n digits */
	for i := base; i < base*10; i++ {
		s := strconv.Itoa(i)
		rev := reverseString(s)
		s += rev[skip:]
		palindromicInteger, _ := strconv.ParseInt(s, 10, 64)
		/* If the current palindrome number is a k-palindromic integer */
		if palindromicInteger%int64(k) == 0 {
			key := getNumKey(int(palindromicInteger))
			if _, ok := keys[key]; ok {
				continue
			}
			comb := countCombination(int(palindromicInteger))
			count += comb
			keys[key] = true

		}
	}

	return count
}

func intPow(a, b int) int {
	result := 1
	for i := 0; i < b; i++ {
		result *= a
	}
	return result
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// @leet end

