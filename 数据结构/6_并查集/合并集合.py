"""
IN：
4 5
M 1 2
M 3 4
Q 1 2
Q 1 3
Q 3 4
OUT：
Yes
No
Yes
"""

N = 100010

p = [0] * N


# 查找根节点，并进行路径优化
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


if __name__ == '__main__':
    n, m = [int(c) for c in input().split()]
    for i in range(1, n + 1):
        p[i] = i

    for _ in range(m):
        op, a, b = [c for c in input().split()]
        a, b = int(a), int(b)
        if op == "M":
            # 将a插入到b中
            p[find(a)] = find(b)
        else:
            if find(a) == find(b):
                print("Yes")
            else:
                print("No")
