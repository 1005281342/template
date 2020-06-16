from random import randint


# 借助额外数组，容易理解
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


# 参考《数据结构与算法基于Python实现》
def quick_sort_p(nums: list, start: int, end: int):
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
    quick_sort_p(nums, start, left - 1)
    quick_sort_p(nums, left + 1, end)


# from acWing by yxc(c++ => python3)
def quick_sort(nums: list, start: int, end: int):
    if start >= end:
        return

    # 双指针
    left, right = start - 1, end + 1

    t = nums[left + ((right - left) >> 1)]

    while left < right:
        left += 1
        while nums[left] < t:
            left += 1

        right -= 1
        while nums[right] > t:
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

    quick_sort(nums, start, right)
    quick_sort(nums, right + 1, end)


if __name__ == '__main__':
    case = [2, 4, 2, 3, 10, 99, 4, 6, 2, 1, 5, 77, 2]
    print(case)
    print(quick_sort_with_help(case))

    print(case)
    quick_sort_p(case, 0, len(case) - 1)
    print(case)

    case = [2, 4, 2, 3, 10, 99, 4, 6, 2, 1, 5, 77, 2]
    print(case)
    quick_sort(case, 0, len(case) - 1)
    print(case)