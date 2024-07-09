import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    height = [*map(int, input().split())]
    dp = [0] * (N+2)

    for _ in range(M):
        a, b, k = map(int, input().split())
        dp[a] += k
        dp[b+1] -= k
    for i in range(1, N+1):
        dp[i] += dp[i-1]
    for i in range(1, N+1):
        dp[i] += height[i-1]
    print(*dp[1:N+1])

solution()
