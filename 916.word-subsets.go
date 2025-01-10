/*
 * @lc app=leetcode id=916 lang=golang
 *
 * [916] Word Subsets
 */

// @lc code=start
package main

/*
  merge all requirements from words2
*/

func wordSubsets(words1 []string, words2 []string) []string {
	ans := []string{}
	requirements := make(map[rune]int)
	for _, w2 := range words2 {
		charMap := make(map[rune]int)
		for _, c2 := range w2 {
			charMap[c2]++
		}
		for k, v := range charMap {
			if v >= requirements[k] {
				requirements[k] = v
			}
		}
	}

	for _, w := range words1 {
		if isSubset(w, requirements) {
			ans = append(ans, w)
		}
	}
	return ans
}

func isSubset(s1 string, requirements map[rune]int) bool {
	s1Map := make(map[rune]int)
	for _, c1 := range s1 {
		s1Map[c1]++
	}

	for k, v := range requirements {
		if s1Map[k] < v {
			return false
		}
	}
	return true
}

// @lc code=end
