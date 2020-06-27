from copy import copy

# n 所有点的数量
# m 所有边的数量
# k 最大访问边数
n, m, k = [int(x) for x in input().split(" ")]

INF = 1e9

# dist
dist = [INF] * (n + 1)
dist[1] = 0

# backup
backup = [INF] * (n + 1)

edges = [[] for _ in range(m)]

for i in range(m):
    edges[i] = [int(x) for x in input().split(" ")]

for _ in range(k):
    backup = copy(edges)
    for i in range(m):
        a, b, w = edges[i]
        dist[b] = min(dist[b], backup[a] + w)

if dist[n] > INF / 2:
    print(-1)
else:
    print(dist[n])
