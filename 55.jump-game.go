/*
 * @lc app=leetcode id=55 lang=golang
 *
 * [55] Jump Game
 */

// @lc code=start
package main

/*
  1. BFS
  2. Backward greedy approach:
  func canJump(nums []int) bool {
    n := len(nums)
    // canReach := make([]bool,n)
    // canReach[n-1]=true
    closestReachablePosition := n-1
    for i:=n-2;i>=0;i--{
        maxJumpsFromHere := nums[i]
        // for j:=1;j<=maxJumpsFromHere && i+j<n ;j++{
        //     if canReach[i+j]{
        //         canReach[i]=true
        //         break
        //     }
        // }
        if i+maxJumpsFromHere>=closestReachablePosition{
            closestReachablePosition = i
        }
    }
    return closestReachablePosition==0
}
*/

/*
type Queue []int

func (q *Queue) Enqueue(val int) {
	*q = append(*q, val)
}

func (q *Queue) Dequeue() (int, error) {
	if len(*q) == 0 {
		return 0, fmt.Errorf("Queue if Empty")
	}
	value := (*q)[0]
	*q = (*q)[1:]
	return value, nil
}

func (q *Queue) IsEmpty() bool {
	return len(*q) == 0
}

func canJump(nums []int) bool {
	// bfs
	n := len(nums)
	visited := make([]bool, n)
	queue := &Queue{}
	queue.Enqueue(0)
	visited[0] = true
	for !queue.IsEmpty() {
		idx, _ := queue.Dequeue()
		steps := nums[idx]
		for i := 1; i <= steps; i++ {
			newIdx := idx + i
			// early return
			if newIdx == n-1 {
				return true
			}
			if newIdx < n && !visited[newIdx] {
				visited[newIdx] = true
				queue.Enqueue(newIdx)
			}
		}
	}
	return visited[n-1]
}*/

func canJump(nums []int) bool {
	n := len(nums)
	closestReachablePosition := n - 1
	for i := n - 2; i >= 0; i-- {
		maxJumpsFromHere := nums[i]
		if i+maxJumpsFromHere >= closestReachablePosition {
			closestReachablePosition = i
		}
	}
	return closestReachablePosition == 0
}

// @lc code=end
