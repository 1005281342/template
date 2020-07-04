import heapq

# 当点的数量n**2 >= 边的数量m时 为稀疏图 使用堆优化Dijkstra
n, m = [int(x) for x in input().split(" ")]

# dist 记录每个点离起点的距离
dist = [float('inf')] * (n + 1)

lst = list()
heapq.heapify(lst)

for _ in range(m):
    a, b, w = [int(x) for x in input().split(" ")]
    # 按照边的权重排序
    heapq.heappush(lst, (w, a, b))

p = [0] * (n + 1)
# 初始化并查集
for i in range(1, n + 1):
    p[i] = i


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


ans = 0
cnt = 0
while lst:
    w, a, b = heapq.heappop(lst)
    a = find(a)
    b = find(b)
    if a != b:
        p[a] = b
        ans += w
        cnt += 1

if cnt < n - 1:
    # 表示没有生成树的方案
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
