# 双指针
def bin_search(nums: list, target: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + ((right - left) >> 1))
        # 说明target在左半部分
        if nums[mid] > target:
            right = mid - 1
        # 说明target在右半部分
        elif nums[mid] < target:
            left = mid + 1
        # 查找到target
        else:
            return mid
    # 未查找到
    return -1


# ACWing 789题
n, q = [int(x) for x in input().strip().split(" ")]
nums = [int(x) for x in input().strip().split(" ")]
for _ in range(q):
    target = int(input().strip())
    start = bin_search(nums, target)
    if start == -1 or start == n - 1:
        print(start, start)
    else:
        end = start
        for num in nums[start + 1:]:
            if num == target:
                end += 1
            else:
                break

        while start >= 0:
            start -= 1
            if nums[start] != target:
                start += 1
                break

        print(start, end)
