# https://www.acwing.com/blog/content/31/
# https://www.acwing.com/solution/content/8235/
# 查找条件存在于左边界 比如 target <= nums[mid], 从左边开始查找
def l_bin_search(left: int, right: int):
    while left < right:
        mid = left + ((right - left) >> 1)
        if check(mid):
            right = mid
            continue
        left = mid + 1
    return left


# 查找条件存在于右边界 比如 target >= nums[mid], 从右边开始查找
def r_bin_search(left: int, right: int):
    while left < right:
        mid = left + ((right - left + 1) >> 1)
        if check(mid):
            left = mid
            continue
        right = mid - 1
    return left


def check(a: int):
    # 根据题意
    pass
