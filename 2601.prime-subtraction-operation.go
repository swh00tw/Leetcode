/*
 * @lc app=leetcode id=2601 lang=golang
 *
 * [2601] Prime Subtraction Operation
 */

// @lc code=start
package main

func primeSubOperation(nums []int) bool {
	/*
	   recursive
	*/
	n := len(nums)
	cachedIsPrime := cached(isPrime)

	var getAns func(idx int, lowerBound int) bool
	getAns = func(idx int, lowerBound int) bool {
		// base case: when idx out of range
		// general case: if the number lower or equal than lowerBound, return false
		// else, try to substract some prime to get as close to lowerBound as possible and keep recursive
		if idx >= n {
			return true
		}
		if nums[idx] <= lowerBound {
			return false
		}
		newLowerBound := nums[idx]
		for i := 2; i < nums[idx]; i++ {
			if cachedIsPrime(i) {
				// try subtract
				possibleLowerBound := nums[idx] - i
				if possibleLowerBound > lowerBound && possibleLowerBound < newLowerBound {
					newLowerBound = possibleLowerBound
				}
			}
		}
		return getAns(idx+1, newLowerBound)
	}

	return getAns(0, 0)
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func cached[T comparable](fn func(T) bool) func(T) bool {
	cache := make(map[T]bool)
	return func(input T) bool {
		if result, exists := cache[input]; exists {
			return result
		}
		result := fn(input)
		cache[input] = result
		return result
	}
}

/*
  Answer 2: https://leetcode.com/problems/prime-subtraction-operation/solutions/3342106/neat-golang-binary-search/?envType=daily-question&envId=2024-11-11
  1. first, list all primes between 2 and 1000
  2. same structure as above, but for finding the best newLowerBound, use binary search
*/

// @lc code=end
