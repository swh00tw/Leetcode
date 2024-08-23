/*
 * @lc app=leetcode id=592 lang=golang
 *
 * [592] Fraction Addition and Subtraction
 */

// @lc code=start
package main

import "fmt"

func GCD(a, b int) int {
	if b == 0 {
		return a
	}
	return GCD(b, a%b)
}

func LCM(a, b int) int {
	return (a * b) / GCD(a, b)
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

type Fraction struct {
	numerator   int // always positive
	denominator int // always positive
	hasSlash    bool
	isPositive  bool
}

func getNewFraction(isPositive bool) *Fraction {
	return &Fraction{
		isPositive: isPositive,
	}
}

func (f *Fraction) ParseNumerator(newChar byte) {
	newNum := int(newChar - '0')
	f.numerator = f.numerator*10 + newNum
}

func (f *Fraction) ParseDenominator(newChar byte) {
	newNum := int(newChar - '0')
	f.denominator = f.denominator*10 + newNum
}

func addTwoFractions(f1 *Fraction, f2 *Fraction) (*Fraction, error) {
	if f1 == nil || f2 == nil {
		return nil, fmt.Errorf("nil fraction")
	}
	d1 := f1.denominator
	d2 := f2.denominator
	lcm := LCM(d1, d2)
	n1 := f1.numerator * (lcm / d1)
	n2 := f2.numerator * (lcm / d2)
	if !f1.isPositive {
		n1 = -n1
	}
	if !f2.isPositive {
		n2 = -n2
	}
	return &Fraction{numerator: abs(n1 + n2), denominator: lcm, isPositive: n1+n2 >= 0}, nil
}

func (f *Fraction) Reduce() {
	// edge case
	if f.numerator == 0 {
		f.denominator = 1
		f.isPositive = true
	}
	gcd := GCD(abs(f.numerator), abs(f.denominator))
	f.numerator = f.numerator / gcd
	f.denominator = f.denominator / gcd
}

func fractionAddition(expression string) string {
	if expression[0] != byte('-') {
		expression = "+" + expression
	}
	// parse
	var currFraction *Fraction
	fractions := make([]*Fraction, 0)
	for i := 0; i < len(expression); i++ {
		char := expression[i]
		if char == byte('-') || char == byte('+') {
			if currFraction != nil {
				fractions = append(fractions, currFraction)
			}
			currFraction = getNewFraction(char == byte('+'))
		} else if char == byte('/') {
			currFraction.hasSlash = true
		} else {
			if currFraction.hasSlash == false {
				currFraction.ParseNumerator(char)
			} else {
				currFraction.ParseDenominator(char)
			}
		}
	}
	if currFraction != nil {
		fractions = append(fractions, currFraction)
	}
	// add
	ans := fractions[0]
	for i := 1; i < len(fractions); i++ {
		ans, _ = addTwoFractions(ans, fractions[i])
	}
	ans.Reduce()
	// return
	ansStr := fmt.Sprintf("%d/%d", ans.numerator, ans.denominator)
	if !ans.isPositive {
		ansStr = fmt.Sprintf("-%s", ansStr)
	}

	return ansStr
}

// @lc code=end
