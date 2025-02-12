/*
 * @lc app=leetcode id=2342 lang=golang
 *
 * [2342] Max Sum of a Pair With Equal Sum of Digits
 */

// @lc code=start
package main

/*
group by sum of digits
*/
func maximumSum(nums []int) int {
	numGroups := make(map[int][]int)
	for _, n := range nums {
		key := getSumOfDigits(n)
		if _, ok := numGroups[key]; !ok {
			numGroups[key] = []int{}
		}
		numGroups[key] = append(numGroups[key], n)
	}

	ans := -1
	for _, v := range numGroups {
		if len(v) < 2 {
			continue
		}
		n1 := v[0]
		n2 := v[1]
		if n1 < n2 {
			n1, n2 = n2, n1
		}
		for i := 2; i < len(v); i++ {
			n := v[i]
			if n > n1 {
				n1, n2 = n, n1
			} else if n > n2 {
				n1, n2 = n1, n
			}
		}
		if n1+n2 > ans {
			ans = n1 + n2
		}
	}
	return ans
}

func getSumOfDigits(num int) int {
	ans := 0
	for num != 0 {
		ans += num % 10
		num /= 10
	}
	return ans
}

// @lc code=end
