n = 100000

e = [0] * n
left = [0] * n
right = [0] * n

# 初始化
# 将节点0作为头节点
# 将节点1作为尾节点
right[0] = 1
# left[0] = -1  # 头节点没有左节点x
left[1] = 0
# right[1] = -1  # 尾节点没有右节点

idx = 2  # 可使用节点从节点2开始


# 在节点a的右边插入一个数x
def insert(a, x):
    global idx
    e[idx] = x

    left[idx] = a
    right[idx] = right[a]

    left[right[a]] = idx
    right[a] = idx
    idx += 1


# 删除节点a
def remove(a):
    right[left[a]] = right[a]
    left[right[a]] = left[a]


if __name__ == '__main__':
    m = int(input())
    for _ in range(m):
        k = x = 0
        t = input().split(" ")
        if t[0] == "L":
            x = int(t[-1])
            insert(0, x)
        elif t[0] == "R":
            x = int(t[-1])
            insert(left[1], x)
        elif t[0] == "D":
            k = int(t[-1])
            remove(k + 1)
        elif t[0] == "IL":
            k, x = int(t[1]), int(t[2])
            insert(left[k + 1], x)
        else:
            k, x = int(t[1]), int(t[2])
            insert(k + 1, x)

    i = right[0]  # 虚拟头节点
    while i != 1:  # 虚拟尾节点
        print(e[i])
        i = right[i]

"""
IN:
10 
R 7
D 1
L 3
IL 2 10
D 3
IL 2 7
L 8
R 9
IL 4 7
IR 2 2
OUT:
8
7
7
3
2
9
"""
