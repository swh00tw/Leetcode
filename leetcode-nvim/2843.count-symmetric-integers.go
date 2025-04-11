package main

// @leet start
func countSymmetricIntegers(low int, high int) int {
	getNumberOfDigits := func(n int) int {
		digits := 0
		for n > 0 {
			digits++
			n = n / 10
		}
		return digits
	}
	isSymmetric := func(n int) bool {
		// first, check if the number of digits is event
		digits := getNumberOfDigits(n)
		if digits%2 == 1 {
			return false
		}
		leftSum, rightSum := 0, 0
		half := digits / 2
		iter := 0
		for n > 0 {
			remainder := n % 10
			if iter < half {
				rightSum += remainder
			} else {
				leftSum += remainder
			}
			iter++
			n = n / 10
		}
		return leftSum == rightSum
	}

	count := 0
	for i := low; i <= high; i++ {
		if isSymmetric(i) {
			count++
		}
	}
	return count
}

// @leet end

