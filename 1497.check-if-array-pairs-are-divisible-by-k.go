/*
 * @lc app=leetcode id=1497 lang=golang
 *
 * [1497] Check If Array Pairs Are Divisible by k
 */

// @lc code=start
package main

func canArrange(arr []int, k int) bool {
	/*
			   convert every number in arr to remainder of k
			   and count freq,
			   iterate 0 to k-1, make sure freq[i] == freq[k-i]
		     special case: i == 0
	*/
	freq := make(map[int]int)
	for _, n := range arr {
		key := ((n % k) + k) % k // transform negative number
		if _, ok := freq[key]; !ok {
			freq[key] = 0
		}
		freq[key]++
	}

	for i := 0; i < k; i++ {
		// special case 1: i == 0
		if i == 0 {
			if freq[i]%2 != 0 {
				return false
			}
			continue
		}
		// special case 2: i == k-1
		if i == k-i {
			if freq[i]%2 != 0 {
				return false
			}
			continue
		}
		if freq[i] != freq[k-i] {
			return false
		}
	}
	return true
}

// @lc code=end
