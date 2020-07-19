n, m = [int(x) for x in input().split(" ")]
q = [[0, 0] for _ in range(m + 1)]  # (pos, val)
dp = [0] * (m + 1)

for _ in range(n):
    v, w, s = [int(x) for x in input().split(" ")]
    for j in range(v):
        hh, tt, stop = 0, 0, (m - j) // v

        for k in range(stop + 1):
            val = dp[k * v + j] - k * w

            while hh < tt and val >= q[tt - 1][1]:
                tt -= 1

            q[tt][0] = k
            q[tt][1] = val
            tt += 1

            if q[hh][0] < k - s:
                hh += 1

            dp[v * k + j] = q[hh][1] + k * w

print(dp[m])
