n, v = [int(x) for x in input().split(" ")]

vi = [0] * (n + 1)
wi = [0] * (n + 1)
si = [0] * (n + 1)

f = [[0] * (n + 1 + v) for _ in range(n + 1 + v)]

for i in range(1, n + 1):
    vi[i], wi[i], si[i] = [int(x) for x in input().split(" ")]

for i in range(1, n + 1):
    for j in range(v + 1):
        for k in range(si[i] + 1):
            if j < vi[i] * k:
                break
            f[i][j] = max(f[i][j], f[i - 1][j - vi[i] * k] + wi[i] * k)
print(f[n][v])
