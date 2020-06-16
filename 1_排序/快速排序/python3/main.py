from random import randint


def quick_sort_with_help(nums: list) -> list:
    if len(nums) <= 1:
        return nums

    rd = randint(0, len(nums) - 1)

    low = list()
    mid = list()
    high = list()

    for a in nums:
        if a < nums[rd]:
            low.append(a)
        elif a > nums[rd]:
            high.append(a)
        else:
            mid.append(a)

    low = quick_sort_with_help(low)
    high = quick_sort_with_help(high)
    low.extend(mid)
    low.extend(high)
    return low


def quick_sort(nums: list, start: int, end: int):
    if start >= end:
        return

    t = nums[end]
    left = start
    right = end - 1

    while left <= right:

        while left <= right and nums[left] < t:
            left += 1
        while left <= right and nums[right] > t:
            right -= 1

        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    nums[left], nums[end] = nums[end], nums[left]
    quick_sort(nums, start, left - 1)
    quick_sort(nums, left + 1, end)


if __name__ == '__main__':
    case = [2, 4, 2, 3, 10, 99, 4, 6, 2, 1, 5, 77, 2]
    print(case)
    print(quick_sort_with_help(case))

    print(case)
    quick_sort(case, 0, len(case)-1)
    print(case)
