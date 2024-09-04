/*
 * @lc app=leetcode id=874 lang=golang
 *
 * [874] Walking Robot Simulation
 */

// @lc code=start
package main

import "fmt"

// ref: https://leetcode.com/problems/walking-robot-simulation/solutions/5734169/go-solution-with-explanation
func robotSim(commands []int, obstacles [][]int) int {
	// Directions: north, east, south, west
	directions := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	dirIndex := 0 // Start facing north

	// Convert obstacles to a set for quick lookup
	obstacleSet := make(map[string]struct{})
	for _, obstacle := range obstacles {
		key := fmt.Sprintf("%d,%d", obstacle[0], obstacle[1])
		obstacleSet[key] = struct{}{}
	}

	x, y := 0, 0 // Start position
	maxDistance := 0

	for _, command := range commands {
		if command == -2 { // Turn left
			dirIndex = (dirIndex + 3) % 4
		} else if command == -1 { // Turn right
			dirIndex = (dirIndex + 1) % 4
		} else { // Move forward k units
			for step := 0; step < command; step++ {
				newX := x + directions[dirIndex][0]
				newY := y + directions[dirIndex][1]
				// Check if the new position is an obstacle
				key := fmt.Sprintf("%d,%d", newX, newY)
				if _, exists := obstacleSet[key]; exists {
					break // Stop moving in this direction if there's an obstacle
				}
				// Update position
				x, y = newX, newY
				// Update maximum distance squared
				maxDistance = max(maxDistance, x*x+y*y)
			}
		}
	}

	return maxDistance
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end
