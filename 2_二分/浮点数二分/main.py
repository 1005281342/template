# 利用浮点数二分求平方根

def sqrt(x):
    left = 0
    right = x
    mid = 0
    while right - left > 1e-8:
        mid = left + ((right - left) / 2)
        if mid * mid >= x:
            right = mid
        else:
            left = mid

    print(mid)


if __name__ == '__main__':

    sqrt(4)
    sqrt(42)