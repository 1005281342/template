package main

func isPerfectSquare(num int) bool {

	var (
		left  int
		right = num
		mid   int
	)

	for left < right {
		mid = left + ((right - left + 1) >> 1)
		if mid*mid > num {
			right = mid - 1
		} else {
			left = mid
		}
	}

	return left*left == num
}
