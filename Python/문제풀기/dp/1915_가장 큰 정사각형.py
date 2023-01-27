import sys
sys.stdin = open('1915_가장 큰 정사각형.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
result = 0

for i in range(1, n):
    for j in range(1, m):
        if graph[i][j] == '1':
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            result = max(result, dp[i][j])
print(result**2)