# 二分图一定不存在奇边环
from collections import defaultdict

# n点的数量，m边的数量
n, m = [int(x) for x in input().split(" ")]

# 存储图
dd = defaultdict(set)

# color 染色数组
color = [0] * (n + 1)

for _ in range(m):
    a, b = [int(x) for x in input().split(" ")]
    dd[a].add(b)
    dd[b].add(a)


def dfs(u, c):
    color[u] = c
    for node in dd[u]:
        if not color[node]:
            if not dfs(node, 3 - c):
                return False
        elif color[node] == c:
            return False
    return True


flag = True
for i in range(1, n + 1):
    if not color[i]:
        if not dfs(i, 1):
            flag = False
            break

print(flag)
"""
IN:
4 4
1 3
1 4
2 3
2 4
OUT:
True
"""