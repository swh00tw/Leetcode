package main

// @leet start

type NumDivisorAndSum struct {
	N int
	S int
}

func sumFourDivisors(nums []int) int {
	known := make(map[int]NumDivisorAndSum)
	ans := 0
	for _, num := range nums {
		if v, ok := known[num]; ok && v.N == 4 {
			ans += v.S
		} else if !ok {
			ndas := getNumberOfDivisors(num)
			if ndas.N == 4 {
				ans += ndas.S
			}
			known[num] = ndas
		}
	}
	return ans
}

func getNumberOfDivisors(num int) NumDivisorAndSum {
	cnt := 0
	x := 1
	s := 0
	for x*x <= num {
		if num%x == 0 {
			if num/x == x {
				cnt++
				s += x
			} else {
				cnt += 2
				s += x
				s += num / x
			}
		}
		x++
	}
	return NumDivisorAndSum{N: cnt, S: s}
}

// @leet end

