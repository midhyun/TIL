import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [0]*(M+1)
obj = []

for i in range(1, N+1):
    V, C, K = map(int, input().split())

    i = 1
    while K > 0:
        cnt = min(i, K)
        obj.append((V*cnt, C*cnt))
        K -= i
        i *= 2

for V, C in obj:
    for i in range(M, V-1, -1):
        dp[i] = max(dp[i], dp[i - V] + C)

print(dp[M])