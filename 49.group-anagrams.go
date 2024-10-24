/*
 * @lc app=leetcode id=49 lang=golang
 *
 * [49] Group Anagrams
 */

// @lc code=start
package main

import "fmt"

/*
for strings, if the freq hashmap if the same, they are anagrams
we can design a func to parse the string, and build the freq map, and map to a string (key)
we can group by the "key" that represent the freq map

if the size of input is n, the size of each str is m
TC: O(nm)
*/
func groupAnagrams(strs []string) [][]string {
	keys := [][]string{}
	for _, s := range strs {
		keys = append(keys, []string{stringToAnagramKey(s), s})
	}

	// hashmap
	ans := [][]string{}
	anagramGroups := make(map[string][]string)
	for _, keyStrPair := range keys {
		k, v := keyStrPair[0], keyStrPair[1]
		if anagramGroups[k] == nil {
			anagramGroups[k] = make([]string, 0)
		}
		anagramGroups[k] = append(anagramGroups[k], v)
	}
	for _, group := range anagramGroups {
		ans = append(ans, group)
	}
	return ans
}

func stringToAnagramKey(s string) string {
	freq := make(map[rune]int)
	for _, c := range s {
		freq[c]++
	}
	key := ""
	for ch := 'a'; ch <= 'z'; ch++ {
		if _, ok := freq[ch]; !ok {
			continue
		}
		v := freq[ch]
		key += string(ch)
		key += fmt.Sprintf("%d", v)
	}
	return key
}

// @lc code=end
