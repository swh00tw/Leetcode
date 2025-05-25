package main

// @leet start
func longestPalindrome(words []string) int {
	// "xy" & "yx" these two words can form part of a palindrome by appending in the front and end
	// so we need to find how many such pairs we have
	// speical word: "xx", this kind of word can be used in the middle or be used with another same word
	getReverse := func(w string) string {
		return string([]byte{w[1], w[0]})
	}
	wordsFreq := make(map[string]int)
	for _, w := range words {
		wordsFreq[w]++
	}
	// type1: "xx" type words, can be used in the middle or with another same word
	// calculate how many pairs
	type1 := 0
	for w, count := range wordsFreq {
		if w[0] == w[1] && count > 1 {
			type1 += count / 2
			wordsFreq[w] = count % 2 // keep the odd count for the middle
		}
	}
	// type2: "xy" & "yx" type words, can be used in pairs
	type2 := 0
	for w, count := range wordsFreq {
		// second case: "xy" & "yx"
		if w[0] != w[1] {
			revW := getReverse(w)
			pairs := min(count, wordsFreq[revW])
			type2 += pairs
		}
	}
	type2 = type2 / 2 // each pair contributes to two words
	pairCount := type1 + type2

	// chjeck if we have a special word that can be used in the middle
	haveMiddle := 0
	for w, count := range wordsFreq {
		if w[0] == w[1] && count == 1 {
			haveMiddle = 1
			break
		}
	}
	return pairCount*4 + haveMiddle*2
}

// @leet end
