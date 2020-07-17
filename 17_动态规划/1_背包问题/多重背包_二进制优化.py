from math import log2

n, v = [int(x) for x in input().split(" ")]
xx = n * (int(log2(v)) + 1)
vi = [0] * xx
wi = [0] * xx

dp = [0] * (v + 1)

cnt = 0
for _ in range(n):
    a, b, c = [int(x) for x in input().split(" ")]
    k = 1
    while c >= k:
        cnt += 1
        vi[cnt] = k * a
        wi[cnt] = k * b
        c -= k
        k *= 2
    if c > 0:
        cnt += 1
        vi[cnt] = c * a
        wi[cnt] = c * b

for i in range(1, cnt + 1):
    for j in range(v, -1, -1):
        if j < vi[i]:
            break
        dp[j] = max(dp[j], dp[j - vi[i]] + wi[i])
print(dp[v])
