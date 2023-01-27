import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e6)
dp = [INF] * (n+1)
dp[1] = 0
for i in range(1, n):
    dp[i+1] = min(dp[i+1], dp[i] + 1)
    try:
        dp[i*2] = min(dp[i*2], dp[i] + 1)
    except: pass
    try:
        dp[i*3] = min(dp[i*3], dp[i] + 1)
    except: pass
print(dp[n])
result = [n]
now = n
temp = dp[n] - 1
for i in range(n, 0, -1):
    if dp[i] == temp and (i+1 == now or i*2 == now or i*3 == now):
        now = i
        result.append(i)
        temp -= 1

print(*result)