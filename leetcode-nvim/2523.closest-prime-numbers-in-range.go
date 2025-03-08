package main

// @leet start
func closestPrimes(left int, right int) []int {
	primes := []int{}
	n := left
	for n <= right {
		if isPrime(n) {
			primes = append(primes, n)
		}
		n++
	}
	if len(primes) < 2 {
		return []int{-1, -1}
	}
	minDiff := primes[1] - primes[0]
	ansIdx := 0
	for i := 0; i < len(primes)-1; i++ {
		if primes[i+1]-primes[i] < minDiff {
			minDiff = primes[i+1] - primes[i]
			ansIdx = i
		}
	}
	return primes[ansIdx : ansIdx+2]
}

func isPrime(n int) bool {
	if n == 1 {
		return false
	}
	if n == 2 {
		return true
	}
	div := 2
	for div*div <= n {
		if n%div == 0 {
			return false
		}
		div++
	}
	return true
}

// @leet end

