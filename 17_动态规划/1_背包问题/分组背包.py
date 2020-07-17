n, v = [int(x) for x in input().split(" ")]
vi = [[0] * (n + 1 + v) for _ in range(n + 1)]
wi = [[0] * (n + 1 + v) for _ in range(n + 1)]
si = [0] * (n + 1)
f = [0] * (v + 1)

for i in range(1, n + 1):
    si[i] = int(input())
    for j in range(si[i]):
        vi[i][j], wi[i][j] = [int(x) for x in input().split(" ")]

for i in range(1, n + 1):
    for j in range(v, -1, -1):
        for k in range(si[i]):
            if vi[i][k] > j:
                continue
            f[j] = max(f[j], f[j - vi[i][k]] + wi[i][k])

print(f[v])
