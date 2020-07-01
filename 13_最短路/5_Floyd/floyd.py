# 查询任意两点之间的最短距离
# n 所有点的数量
# m 所有边的数量
# q 查询次数
n, m, q = [int(x) for x in input().split(" ")]

d = [[float('inf')] * (n + 1) for _ in range(n + 1)]


def floyd():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


for _ in range(m):
    a, b, w = [int(x) for x in input().split(" ")]
    d[a][b] = min(d[a][b], w)

floyd()

for _ in range(q):
    a, b = [int(x) for x in input().split(" ")]
    if d[a][b] == float('inf'):
        print(-1)
    else:
        print(d[a][b])
