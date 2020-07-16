n, v = [int(x) for x in input().split(" ")]
f = [[0] * (n + 1 + v) for _ in range(n + 1 + v)]
vi = [0] * (n + 1)
wi = [0] * (n + 1)

for i in range(1, n + 1):
    vi[i], wi[i] = [int(x) for x in input().split(" ")]

# 从前i可物品中选
for i in range(1, n + 1):
    for j in range(v + 1):
        # f[i][j] = f[i - 1][j]
        for k in range(j + 1):
            if j < vi[i] * k:
                break
            f[i][j] = max(f[i][j], f[i - 1][j - vi[i] * k] + wi[i] * k)

print(f[n][v])

# 注意数据加强后朴素做法已经不能过了
