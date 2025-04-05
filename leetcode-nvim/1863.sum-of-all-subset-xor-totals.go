package main

// @leet start
func subsetXORSum(nums []int) int {
	n := len(nums)
	var getSubsetSums func(idx int) []int
	getSubsetSums = func(idx int) []int {
		if idx == 0 {
			return []int{nums[idx]}
		}
		sums := getSubsetSums(idx - 1)
		ans := []int{}
		ans = append(ans, sums...)
		for _, sum := range sums {
			ans = append(ans, sum^nums[idx])
		}
		ans = append(ans, nums[idx])
		return ans
	}
	sums := getSubsetSums(n - 1)
	ans := 0
	for _, sum := range sums {
		ans += sum
	}
	return ans
}

// @leet end

