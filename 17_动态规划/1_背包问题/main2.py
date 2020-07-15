n, v = [int(x) for x in input().split(" ")]
f = [0] * (n + 1 + v)
ws = [0] * (n + 1)
vs = [0] * (n + 1)

for i in range(1, n + 1):
    vs[i], ws[i] = [int(x) for x in input().split(" ")]

for i in range(1, n + 1):
    for j in range(v, vs[i] - 1, -1):
        f[j] = max(f[j], f[j - vs[i]] + ws[i])
print(f[n][v])
