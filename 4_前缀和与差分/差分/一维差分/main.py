"""
# 查分适用场景
给你一串长度为n的数列a1,a2,a3......an，要求对a[L]~a[R]进行m次操作：
操作一：将a[L]~a[R]内的元素都加上P
操作二：将a[L]~a[R]内的元素都减去P

[参考](https://www.jianshu.com/p/fcb68475b5e4)

查分是前缀和的逆运算
原数组：a1, a2, a3, a4
查分数组：b1 = a1
        b2 = a2 - a1
        b3 = a3 - a2
        b4 = a4 - a3
即满足：a1 = b1
       a2 = b1 + b2
       a3 = b1 + b2 + b3
       a4 = b1 + b2 + b3 + b4
"""

# https://www.acwing.com/problem/content/description/799/
t, n = [int(c) for c in input().split(" ")]
sums = [int(c) for c in input().split(" ")]
nums = [0] * (len(sums) + 10)


def add(l, r, c):
    nums[l] += c
    nums[r + 1] -= c


# 构造查分数组
for i, num in enumerate(sums):
    add(i + 1, i + 1, num)

for _ in range(n):

    l, r, c = [int(c) for c in input().split(" ")]
    add(l, r, c)
    # 还原数组（从查分数组还原数据），进行前缀和计算
    for i in range(1, t + 1):
        nums[i] += nums[i - 1]

ans = ""
for i in range(1, t):
    ans += str(nums[i]) + " "
ans += str(nums[t])

print(ans)