n, v = [int(x) for x in input().split(" ")]
f = [[0] * (n + 1 + v) for _ in range(n + 1 + v)]
ws = [0] * (n + 1)
vs = [0] * (n + 1)

for i in range(1, n + 1):
    vs[i], ws[i] = [int(x) for x in input().split(" ")]

for i in range(1, n + 1):
    for j in range(0, v + 1):
        f[i][j] = f[i - 1][j]
        if j >= vs[i]:
            f[i][j] = max(f[i][j], f[i - 1][j - vs[i]] + ws[i])
print(f[n][v])
