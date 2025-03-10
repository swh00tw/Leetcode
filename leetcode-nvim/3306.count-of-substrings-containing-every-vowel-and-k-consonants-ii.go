package main

import (
	"slices"
)

// @leet start
// ref: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/solutions/6501738/count-of-substrings-containing-every-vowel-and-k-consonants-ii
var vowels = []byte{'a', 'e', 'i', 'o', 'u'}

func isVowel(c byte) bool {
	return slices.Contains(vowels, c)
}

func countOfSubstrings(word string, k int) int64 {
	// sliding window
	// keep a dictionary to store the count of each character
	// if dict's len is 5, and window size - len(dict) = k, we find a valid substring
	// keep moving r, until consonants more than k, if that happen, move l
	vowelCount := make(map[byte]int)
	totalVowels := 0
	l, r := 0, 0
	ans := int64(0)

	idx := len(word)
	nextConsonantIdx := make([]int, len(word))
	for i := len(word) - 1; i >= 0; i-- {
		nextConsonantIdx[i] = idx
		if !isVowel(word[i]) {
			idx = i
		}
	}

	for r < len(word) {
		if isVowel(word[r]) {
			vowelCount[word[r]]++
			totalVowels++
		}
		for (r-l+1)-totalVowels > k {
			// move l
			if isVowel(word[l]) {
				totalVowels--
				vowelCount[word[l]]--
				if vowelCount[word[l]] == 0 {
					delete(vowelCount, word[l])
				}
			}
			l++
		}
		// find next consonant idx, add nextConsonantIdx - r to ans
		// try to shrink the window if it's valid
		for l < len(word) && len(vowelCount) == 5 && r-l+1-totalVowels == k {
			ans += int64(nextConsonantIdx[r] - r)
			if isVowel(word[l]) {
				totalVowels--
				vowelCount[word[l]]--
				if vowelCount[word[l]] == 0 {
					delete(vowelCount, word[l])
				}
			}
			l++
		}
		r++
	}
	return ans
}

// @leet end

