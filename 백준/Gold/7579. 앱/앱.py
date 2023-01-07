import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memories =[0] + [*map(int, input().split())]
cost =[0] + [*map(int, input().split())]
length = sum(cost) + 1
dp = [[0]*length for _ in range(n+1)]
ans = 1e9

for i in range(1, n+1):
    cost_i, memory_i = cost[i], memories[i]
    for j in range(cost_i+1):
        dp[i][j] = dp[i-1][j]
    for j in range(cost_i, length):
        dp[i][j] = max(dp[i-1][j-cost_i] + memory_i, dp[i-1][j])
        if dp[i][j] >= m:
            ans = min(ans, j)

print(ans)