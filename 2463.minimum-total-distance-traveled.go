/*
 * @lc app=leetcode id=2463 lang=golang
 *
 * [2463] Minimum Total Distance Traveled
 */

// @lc code=start
package main

import (
	"fmt"
	"math"
	"sort"
)

/*
2 pointers,
p1 point to sorted robot arr
p2 point to sorted factory arr
compare the combination of (p1, p2), (p1, p2+1) if p1 is at the right side of p2
tie-break: choose (p1, p2)
if choose (p1, p2) --> move to (p1+1, p2)
else, move to (p1+1, p2+1)
*/
func minimumTotalDistance(robot []int, factory [][]int) int64 {
	sort.Slice(robot, func(i, j int) bool {
		return robot[i] < robot[j]
	})
	sort.Slice(factory, func(i, j int) bool {
		return factory[i][0] < factory[j][0]
	})
	fmt.Println(robot)
	fmt.Println(factory)

	cache := make(map[string]int64)

	var getAns func(p1, p2 int) int64
	getAns = func(p1, p2 int) int64 {
		key := getCachekey(p1, p2)
		if _, ok := cache[key]; ok {
			return cache[key]
		}
		// base case
		if p1 == len(robot) {
			return 0
		}
		if p2 == len(factory) {
			return int64(math.Pow(10, 15)) // magic big number
		}
		// case 0, this factory don't take any robot
		ans := getAns(p1, p2+1)
		// other cases, take 1, 2, 3, ... until limit
		var total_dis int64 = 0
		for i := 0; i < factory[p2][1]; i++ {
			if p1+i < len(robot) {
				total_dis += abs(int64(robot[p1+i] - factory[p2][0]))
				possibleAns := total_dis + getAns(p1+i+1, p2+1)
				if possibleAns < ans {
					ans = possibleAns
				}
			} else {
				break
			}
		}

		cache[key] = ans
		return ans
	}

	ans := getAns(0, 0)

	return ans
}

func getCachekey(p1, p2 int) string {
	return fmt.Sprintf("%d,%d", p1, p2)
}

func abs(ans int64) int64 {
	if ans < 0 {
		return (-1) * ans
	}
	return ans
}
