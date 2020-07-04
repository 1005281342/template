# https://www.acwing.com/problem/content/description/852/
import heapq
from collections import defaultdict

# 当点的数量n**2 >= 边的数量m时 为稀疏图 使用堆优化Dijkstra
n, m = [int(x) for x in input().split(" ")]

dd = defaultdict(set)

# dist 记录每个点离起点的距离
dist = [float('inf')] * (n + 1)

# st 该点最短路是否已确定
st = [False] * (n + 1)

for _ in range(m):
    a, b, c = [int(x) for x in input().split(" ")]
    dd[a].add((b, c))

# 起点为1号点
dist[1] = 0
hq = [(0, 1)]  # (和起点的距离, 第几个点)
heapq.heapify(hq)

while hq:
    # 优先处理边距短的点
    dis, node = heapq.heappop(hq)
    if st[node]:
        continue
    st[node] = True

    # 处理每条边
    for new_node, wight in dd[node]:
        if dist[new_node] > dist[node] + wight:
            dist[new_node] = dist[node] + wight
            heapq.heappush(hq, (dist[new_node], new_node))

if dist[n] == float('inf'):
    print(-1)
else:
    print(dist[n])
