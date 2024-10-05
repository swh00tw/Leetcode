/*
 * @lc app=leetcode id=2491 lang=golang
 *
 * [2491] Divide Players Into Teams of Equal Skill
 */

// @lc code=start
package main

/*
  calculate the sum of array first, the sum of each time must be (sum/n)*2
  use hashmap to store val to freq, start pairing
*/

func dividePlayers(skill []int) int64 {
	s := 0
	n := len(skill)
	for _, num := range skill {
		s += num
	}
	k := 2 * s / n
	freq := make(map[int]int)
	pairs := make([][]int, 0)
	for _, num := range skill {
		rest := k - num
		if val, ok := freq[rest]; ok && val > 0 {
			freq[rest]--
			pairs = append(pairs, []int{num, rest})
		} else {
			freq[num]++
		}
	}
	if len(pairs) != n/2 {
		return -1
	}
	ans := int64(0)
	for _, p := range pairs {
		ans += int64(p[0] * p[1])
	}
	return ans
}

// @lc code=end
