package main

// @leet start
const MOD = 1000000007 // 10^9 + 7

// primeFactorize returns the prime factorization of m as a map of prime factors to their counts
func primeFactorize(m int) map[int]int {
	factors := make(map[int]int)
	divisor := 2

	for m > 1 {
		for m%divisor == 0 {
			factors[divisor]++
			m /= divisor
		}
		divisor++

		// Optimization: if divisor^2 > m, then m is prime
		if divisor*divisor > m && m > 1 {
			factors[m]++
			break
		}
	}

	return factors
}

// modInverse calculates the modular multiplicative inverse of a modulo MOD
func modInverse(a int) int {
	return modPow(a, MOD-2)
}

// modPow calculates (base^exponent) % MOD efficiently
func modPow(base, exponent int) int {
	result := 1
	base %= MOD

	for exponent > 0 {
		if exponent%2 == 1 {
			result = (result * base) % MOD
		}
		exponent >>= 1
		base = (base * base) % MOD
	}

	return result
}

// combinations calculates the binomial coefficient C(n,k) % MOD
func combinations(n, k int) int {
	if k < 0 || k > n {
		return 0
	}
	if k == 0 || k == n {
		return 1
	}

	// Use the smaller of k and n-k for efficiency
	if k > n-k {
		k = n - k
	}

	// Calculate using the formula C(n,k) = n! / (k! * (n-k)!)
	// But to avoid overflow, we calculate this modulo MOD
	numerator := 1
	denominator := 1

	for i := 1; i <= k; i++ {
		numerator = (numerator * (n - (k - i))) % MOD
		denominator = (denominator * i) % MOD
	}

	// Use Fermat's little theorem to calculate modular inverse
	return (numerator * modInverse(denominator)) % MOD
}

// countDistributions calculates the number of unique arrays of length n given number m
func countDistributions(n, m int) int {
	// Get prime factorization
	factorCounts := primeFactorize(m)

	// Calculate using stars and bars formula
	result := 1

	for _, count := range factorCounts {
		// For each distinct prime factor p^k, calculate C(n+k-1, k)
		comb := combinations(n+count-1, count)
		result = (result * comb) % MOD
	}

	return result
}

func idealArrays(n int, maxValue int) int {
	// count the number of ideal arrays for each starting number
	// imagine we have a "multiple array" where m[i] = arr[i+1]/arr[i] where has length of n-1
	// we can try to multiple the starting number from 1 to x until it exceeds maxValue
	// for example, if multiplying 2 is valid, the number of idealArrays can be calculated like this
	// the factors can choose which index it wants to be
	// so, for each multiple, need to know how many factors it has
	// and the num of unqiue "mutlple arrays" => prime factorization and distribute the factor from index 0 to n-2
	// to perform such calculation, use "countDistributions" function
	// if the sum of the power of the prime factors is k, the answer should be incremented by (n-1)^k

	ans := 0

	for start := 1; start <= maxValue; start++ {
		ans++
		multiples := 2
		for multiples*start <= maxValue {
			inc := countDistributions(n-1, multiples)
			ans += inc
			multiples++
		}
	}
	return ans % MOD
}

// @leet end

