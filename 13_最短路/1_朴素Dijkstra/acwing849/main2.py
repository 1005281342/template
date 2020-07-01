# https://www.acwing.com/problem/content/description/851/
from collections import defaultdict

n, m = [int(x) for x in input().split(" ")]

dd = defaultdict(set)
for _ in range(m):
    a, b, w = [int(x) for x in input().split(" ")]
    dd[a].add((b, w))

# 每个点到起点的距离
dist = [float('inf')] * (n + 1)
# 起点为1号点
dist[1] = 0

# 该点的最短路是否已经确定
st = [False] * (n + 1)

for _ in range(n):
    # t 存储当前访问的点
    t = -1

    # 题目中点的标识从1开始
    for i in range(1, n + 1):
        if not st[i] and (t == -1 or dist[t] > dist[i]):
            t = i

    st[t] = True

    # 依次更新每个点到相邻点的路径值
    for b, w in dd[t]:
        dist[b] = min(dist[b], dist[t] + w)

if dist[n] == float('inf'):
    print(-1)
else:
    print(dist[n])
