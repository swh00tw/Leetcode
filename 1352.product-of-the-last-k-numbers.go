/*
 * @lc app=leetcode id=1352 lang=golang
 *
 * [1352] Product of the Last K Numbers
 */

// @lc code=start
package main

// https://leetcode.com/problems/product-of-the-last-k-numbers/solutions/6389840/product-of-the-last-k-numbers

type ProductOfNumbers struct {
	size        int
	leftProduct []int // leftProduct[i] => product of nums[:i]
}

func Constructor() ProductOfNumbers {
	return ProductOfNumbers{
		leftProduct: []int{1},
		size:        0,
	}
}

func (this *ProductOfNumbers) Add(num int) {
	if num == 0 {
		this.leftProduct = []int{1}
		this.size = 0
	} else {
		this.leftProduct = append(this.leftProduct, this.leftProduct[this.size]*num)
		this.size++
	}
}

func (this *ProductOfNumbers) GetProduct(k int) int {
	if k > this.size {
		return 0
	}
	return this.leftProduct[this.size] / this.leftProduct[this.size-k]
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(num);
 * param_2 := obj.GetProduct(k);
 */
// @lc code=end
