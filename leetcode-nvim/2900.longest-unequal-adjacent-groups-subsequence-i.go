package main

// @leet start

type SequenceGroup struct {
	groupIdx int
	words    []string
	next     *SequenceGroup
}

func getNewSequenceGroups(idx int) *SequenceGroup {
	g := SequenceGroup{
		idx,
		[]string{},
		nil,
	}
	return &g
}

func getLongestSubsequence(words []string, groups []int) []string {
	currGroup := getNewSequenceGroups(groups[0])
	head := currGroup
	n := len(words)
	for i := 0; i < n; i++ {
		currWord := words[i]
		groupIdx := groups[i]
		if currGroup.groupIdx != groupIdx {
			nextGroup := getNewSequenceGroups(groupIdx)
			nextGroup.words = append(nextGroup.words, currWord)
			currGroup.next = nextGroup
			currGroup = nextGroup
		} else {
			currGroup.words = append(currGroup.words, currWord)
		}
	}
	ans := []string{}
	group := head
	for group != nil {
		ans = append(ans, group.words[0])
		group = group.next
	}
	return ans
}

// @leet end

