n, v = [int(x) for x in input().split(" ")]
f = [0] * (v + 1)
vi = [0] * (n + 1)
wi = [0] * (n + 1)

for i in range(1, n + 1):
    vi[i], wi[i] = [int(x) for x in input().split(" ")]

# 从前i可物品中选
for i in range(1, n + 1):
    for j in range(vi[i], v + 1):
        f[j] = max(f[j], f[j - vi[i]] + wi[i])
print(f[v])

# 注意数据加强后朴素做法已经不能过了
