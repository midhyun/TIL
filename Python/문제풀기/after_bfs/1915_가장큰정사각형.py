import sys
sys.stdin = open('1915_가장큰정사각형.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
graph =[[0]*(m+1)]
for _ in range(n):
    graph.append([0] + list(input().strip()))
dp = [[0]*(m+1) for _ in range(n+1)]

result = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == '1': 
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            result = max(result, dp[i][j])

print(result**2)