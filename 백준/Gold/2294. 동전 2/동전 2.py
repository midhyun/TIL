import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [10001]*(k+1)
dp[0] = 0
for v in coins:
    for j in range(v, k+1):
        dp[j] = min(dp[j-v]+1, dp[j])
if dp[k] >= 10001:
    print(-1)
else:
    print(dp[k])