n, v, m = [int(x) for x in input().split()]

dp = [[0] * (m + 1) for _ in range(v + 1)]

for _ in range(n):
    a, b, c = [int(x) for x in input().split()]
    for j in range(v, a - 1, -1):
        for k in range(m, b - 1, -1):
            dp[j][k] = max(dp[j][k], dp[j - a][k - b] + c)

print(dp[v][m])
