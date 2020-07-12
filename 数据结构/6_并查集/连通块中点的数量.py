N = 100010

p = [0] * N
cnt = [1] * N


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
        recv = input().split(" ")
        op = recv[0]
        if op == "C":
            a, b = int(recv[1]), int(recv[2])
            a = find(a)
            b = find(b)
            if a != b:
                # 将a插入到节点b中
                p[a] = b
                # 维护根节点连通块中的数量
                cnt[b] += a
        elif op == "Q1":
            a, b = int(recv[1]), int(recv[2])
            if find(a) == find(b):
                print("Yes")
            else:
                print("No")
        else:
            a = int(recv[1])
            print(cnt[find(a)])

"""
IN:
5 5
C 1 2
Q1 1 2
Q2 1
C 2 5
Q2 5
OUT:
Yes
2
3
"""
