/*
 * @lc app=leetcode id=128 lang=golang
 *
 * [128] Longest Consecutive Sequence
 */

// @lc code=start
package main

/*
First, we remove duplicate from nums
Second, we use hashmap to store mapping from number to index
This requires O(n) time to build this map.
Next, for each num in nums (linear traverse),
we do BFS to find the longest sequence this number link to using the hashmap we build
(we need visited array to store whether the number is visted or not to avoid duplication)
*/
func longestConsecutive(nums []int) int {
	newNums := []int{}
	seen := make(map[int]bool)
	for _, n := range nums {
		if seen[n] {
			continue
		}
		seen[n] = true
		newNums = append(newNums, n)
	}

	num2Idx := make(map[int]int)
	for i, n := range newNums {
		num2Idx[n] = i
	}

	visited := make([]bool, len(newNums))
	ans := 0
	for i, n := range newNums {
		if visited[i] {
			continue
		}
		// BFS
		seq := 0
		visited[i] = true
		q := []int{n}
		for len(q) > 0 {
			// pop
			val := q[0]
			q = q[1:]
			seq++
			// neighbors
			if neighborIdx, ok := num2Idx[val+1]; ok {
				if !visited[neighborIdx] {
					visited[neighborIdx] = true
					q = append(q, newNums[neighborIdx])
				}
			}
			if neighborIdx, ok := num2Idx[val-1]; ok {
				if !visited[neighborIdx] {
					visited[neighborIdx] = true
					q = append(q, newNums[neighborIdx])
				}
			}
		}
		if seq > ans {
			ans = seq
		}
	}
	return ans
}

// @lc code=end
