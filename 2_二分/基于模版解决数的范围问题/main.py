# ACWing 789题
n, q = [int(x) for x in input().strip().split(" ")]
nums = [int(x) for x in input().strip().split(" ")]
for _ in range(q):
    target = int(input().strip())
    left = 0
    right = n - 1
    # 从左边查找目标值
    while left < right:
        mid = left + ((right - left) >> 1)
        # 目标值在左边
        if nums[mid] >= target:
            right = mid
            continue
        # 目标值在右边
        left = mid + 1

    # 未查找到目标值
    if nums[left] != target:
        print(-1, -1)
        continue

    # 从右边开始查找目标值
    start = left
    left = 0
    right = n - 1
    while left < right:
        mid = left + ((right - left + 1) >> 1)
        # 目标值在右边
        if nums[mid] <= target:
            left = mid
            continue
        # 目标值在左边
        right = mid - 1
    print(start, left)
