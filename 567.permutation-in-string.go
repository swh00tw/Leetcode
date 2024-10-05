/*
 * @lc app=leetcode id=567 lang=golang
 *
 * [567] Permutation in String
 */

// @lc code=start
package main

import "fmt"

/*
get freq of s1
two pointer with recycle
*/
func checkInclusion(s1 string, s2 string) bool {
	freq := make(map[rune]int)
	for _, l := range s1 {
		freq[l]++
	}
	i := 0
	for j := 0; j < len(s2); j++ {
		key := rune(s2[j])
		if val, ok := freq[key]; !ok {
			// recycle
			for i < j {
				if _, ins1 := freq[rune(s2[i])]; ins1 {
					freq[rune(s2[i])]++
				}
				i++
			}
			i++
		} else {
			if val == 0 {
				// recycle, move i
				for i < j {
					if s2[i] == s2[j] {
						break
					}
					if _, ins1 := freq[rune(s2[i])]; ins1 {
						freq[rune(s2[i])]++
					}
					i++
				}
				i++
			} else {
				freq[key]--
			}
		}
		if j-i == len(s1)-1 {
			fmt.Println(i, j)
			return true
		}
	}
	return false
}

// @lc code=end
