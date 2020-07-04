n, m = [int(x) for x in input().split(" ")]

# g 稠密图（m>n**2, 即边的数量大于点的数量）使用邻接矩阵进行存储
g = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, w = [int(x) for x in input().split(" ")]
    # 自环
    if a == b:
        continue
    g[a][b] = g[b][a] = min(g[a][b], w)

# 每个点到起点的距离
dist = [float('inf')] * (n + 1)

# 集合
st = set()

ans = 0

for x in range(n):
    # t 存储当前访问的点
    t = -1

    # 题目中点的标识从1开始
    for i in range(1, n + 1):
        if i not in st and (t == -1 or dist[t] > dist[i]):
            t = i

    if x and dist[t] == float('inf'):
        ans = float('inf')
        break
    if x:
        ans += dist[t]
    st.add(t)

    # 使用t去更新其他点到集合的距离
    for i in range(1, n + 1):
        dist[i] = min(dist[i], g[t][i])

if ans == float('inf'):
    print(-1)
else:
    print(ans)

"""
IN: 
4 5
1 2 1
1 3 2
1 4 3
2 3 2
3 4 4
OUT:
6
"""