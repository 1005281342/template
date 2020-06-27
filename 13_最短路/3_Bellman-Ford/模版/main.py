from copy import copy

# n 所有点的数量
# m 所有边的数量
# k 最大访问边数
n, m = [int(x) for x in input().split(" ")]

INF = 1e9

# dist
dist = [INF] * (n + 1)
dist[1] = 0

# backup
backup = [INF] * (n + 1)

edges = [[] for _ in range(m)]

for i in range(m):
    edges[i] = [int(x) for x in input().split(" ")]

#  如果第n次迭代仍然会松弛三角不等式，就说明存在一条长度是n+1的最短路径，
#  由抽屉原理，路径中至少存在两个相同的点，说明图中存在负权回路。
for _ in range(n):
    backup = copy(edges)
    for i in range(m):
        a, b, w = edges[i]
        dist[b] = min(dist[b], backup[a] + w)

if dist[n] > INF / 2:
    print(-1)
else:
    print(dist[n])
