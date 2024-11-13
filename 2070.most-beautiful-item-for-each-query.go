/*
 * @lc app=leetcode id=2070 lang=golang
 *
 * [2070] Most Beautiful Item for Each Query
 */

// @lc code=start
package main

import (
	"sort"
)

/*
sort based on price, if price the same, sort based on beauty
make a array to store max beauty seen so far (in left side)
for each query, apply binary search
*/
func maximumBeauty(items [][]int, queries []int) []int {
	_items := make([][]int, len(items))
	copy(_items, items)
	sort.Slice(_items, func(i, j int) bool {
		if _items[i][0] == _items[j][0] {
			return _items[i][1] < _items[j][1]
		}
		return _items[i][0] < _items[j][0]
	})

	curr := 0
	mostBeauty := make([]int, len(items))
	for i, item := range _items {
		beauty := item[1]
		if beauty >= curr {
			curr = beauty
		}
		mostBeauty[i] = curr
	}

	res := make([]int, len(queries))
	for i, q := range queries {
		// binary search find rightmost item
		l, r := 0, len(items)-1
		for l <= r {
			m := (l + r) / 2
			if _items[m][0] > q {
				r = m - 1
			} else {
				l = m + 1
			}
		}
		if l-1 >= 0 {
			res[i] = mostBeauty[l-1]
		} else {
			res[i] = 0
		}
	}
	return res
}

// @lc code=end
