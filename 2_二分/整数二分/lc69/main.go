package main

func mySqrt(x int) int {

	var (
		left  int
		right int = x
		mid   int
	)

	for left < right {
		mid = left + ((right - left + 1) >> 1)
		if x < mid*mid {
			right = mid - 1
		} else {
			left = mid
		}
	}
	return left
}
