import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
for i in range(n):
    a, b = map(int, input().split())
    if i+a-1 < n:
        dp[i+a-1] = max(dp[i+a-1], dp[i-1] + b)
    dp[i] = max(dp[i-1], dp[i])
print(dp[n-1])