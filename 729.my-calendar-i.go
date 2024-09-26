/*
 * @lc app=leetcode id=729 lang=golang
 *
 * [729] My Calendar I
 */

// @lc code=start
package main

import (
	"fmt"
	"slices"
)

/*
  The data structure store sorted event by start time
  and store the end time of every events
*/

type MyCalendar struct {
	events        [][]int
	latestEndtime int
}

func Constructor() MyCalendar {
	events := make([][]int, 0)
	latestEndtime := 0
	return MyCalendar{
		events:        events,
		latestEndtime: latestEndtime,
	}
}

func (this *MyCalendar) Show() {
	fmt.Println("events: ", this.events)
	fmt.Println("latestEndtime", this.latestEndtime)
}

// case 1: if start time >= latestEndtime, insert to end
// case 2: binary search and see if it can fit
// update latestEndtime before return
func (this *MyCalendar) Book(start int, end int) bool {
	if start >= this.latestEndtime {
		this.events = append(this.events, []int{start, end})
		this.latestEndtime = end
		return true
	}
	n := len(this.events)
	l, r := 0, len(this.events)-1
	for l <= r {
		m := (l + r) / 2
		if this.events[m][0] == start {
			l = m + 1
			break
		}
		if this.events[m][0] > start {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	canFit := true
	if l > 0 {
		prev := this.events[l-1]
		if start < prev[1] {
			canFit = false
		}
	}
	if l < n {
		next := this.events[l]
		if end > next[0] {
			canFit = false
		}
	}
	if !canFit {
		return false
	}
	// insert
	this.events = slices.Insert(this.events, l, []int{start, end})
	// update
	if end > this.latestEndtime {
		this.latestEndtime = end
	}
	return true
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
// @lc code=end
