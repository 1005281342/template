n = 100000

head = -1  # 虚拟头节点
idx = 0  # 当前可使用点的下标（指针）


# 将x插入到头节点前面
def add_to_head(x):
    global idx
    global head
    e[idx] = x
    ne[idx] = head
    head = idx
    idx += 1


# 将x插入到下标为k的点的后面
def add(k, x):
    global idx
    e[idx] = x
    ne[idx] = ne[k]
    ne[k] = idx
    idx += 1


# 将下标为k的点的后面第一个点移除
def remove(k):
    ne[k] = ne[ne[k]]


if __name__ == '__main__':
    e = [0] * n  # 初始化值数组
    ne = [-1] * n  # 初始化指针数组

    m = int(input())
    for _ in range(m):
        k = x = 0
        t = input()
        # 将x插入到头节点
        if t[0] == "H":
            x = int(t.split(" ")[-1])
            add_to_head(x)
        elif t[0] == "D":  # 移除第k个点，下标为k-1
            k = int(t.split(" ")[-1])
            if k == 0:  # 移除头节点
                head = ne[head]
                continue
            remove(k - 1)
        else:
            k, x = [int(x) for x in t.split(" ")[1:]]
            add(k - 1, x)

    i = head
    while i != -1:
        print(e[i])
        i = ne[i]
"""
IN:
10
H 9
I 1 1
D 1
D 0
H 6
I 3 6
I 4 5
I 4 5
I 3 4
D 6
OUT:
6
4
6
5
"""