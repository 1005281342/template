# https://www.acwing.com/problem/content/description/853/
from collections import defaultdict, deque

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

# dq
dq = deque()
dq.append(1)
st[1] = True

while dq:
    node = dq.popleft()
    st[node] = False

    # 处理每条边
    for new_node, wight in dd[node]:
        if dist[new_node] > dist[node] + wight:
            dist[new_node] = dist[node] + wight
            if not st[new_node]:
                dq.append(new_node)
                st[new_node] = True

if dist[n] == float('inf'):
    print("impossible")
else:
    print(dist[n])
