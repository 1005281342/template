from math import log2

n, m = [int(x) for x in input().split()]

f = [0] * (m + 1)

xx = n * (int(log2(m)) + 1)
a = [0] * xx
b = [0] * xx
c = [False] * xx  # False: 完全背包，True 0-1背包

index = 0

for _ in range(n):
    v, w, s = [int(x) for x in input().split()]
    if s == 0:
        a[index] = v
        b[index] = w
        index += 1
    else:
        if s == -1:
            s = 1
        k = 1
        while k <= s:
            a[index] = k * v
            c[index] = True
            b[index] = k * w
            index += 1
            s -= k
            k <<= 1

        if s:
            a[index] = s * v
            c[index] = True
            b[index] = s * w
            index += 1

for i in range(index):
    if c[i]:
        for j in range(m, a[i] - 1, -1):
            f[j] = max(f[j], f[j - a[i]] + b[i])
    else:
        for j in range(a[i], m + 1):
            f[j] = max(f[j], f[j - a[i]] + b[i])

print(f[m])
