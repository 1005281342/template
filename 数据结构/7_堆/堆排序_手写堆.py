size = 0

n, m = [int(x) for x in input().split(" ")]
h = [-1] + [int(c) for c in input().split(" ")]
size = n


def down(u: int):
    t = u
    if 2 * u <= size and h[2 * u] < h[t]:
        t = 2 * u
    if 2 * u + 1 <= size and h[2 * u + 1] < h[t]:
        t = 2 * u + 1
    if t != u:
        h[t], h[u] = h[u], h[t]
        down(t)


def up(u: int):
    while u >> 1 and h[u >> 1] > h[u]:
        h[u], h[u >> 1] = h[u >> 1], h[u]
        u >>= 1


for i in range(size >> 1, 0, -1):
    down(i)

for _ in range(m):
    print(h[1])
    h[1] = h[size]
    size -= 1
    down(1)
