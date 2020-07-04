from collections import defaultdict

# n代表左半部点的个数，m代表边数
n, _, m = [int(x) for x in input().split(" ")]

dd = defaultdict(set)

# 邻接表 存储图
for _ in range(m):
    a, b = [int(x) for x in input().split(" ")]
    # 只需要处理单向匹配就好了（左半部匹配右半部）
    dd[a].add(b)
    # 如果考虑从右半部匹配左半部则为dd[b] = a，并且需要从右半部开始遍历

# st 标识该点是否已存在匹配关系
st = set()

# match 存储匹配关系 idx: 第idx点，match[idx]: 所匹配的点
match = [0] * (n + 1)

ans = 0


def find(x):
    for node in dd[x]:
        # 如果不存在匹配关系（还未匹配）
        if node not in st:
            st.add(node)
            # 如果x的可选列表中的元素node还未匹配 或者 已匹配关系可以解除
            if match[node] == 0 or find(match[node]):
                match[node] = x
                return 1
    return 0


# 遍历点，从第一个点开始
for i in range(1, n + 1):
    ans += find(i)

print(ans)

"""
IN:
2 2 4
1 1
1 2
2 1
2 2
OUT:
2
"""
