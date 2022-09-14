import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('1520_내리막길.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(i, j):
    if i == n-1 and j == m-1:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    ways = 0
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= x < m and 0 <= y < n:
            if graph[i][j] > graph[y][x]:
                ways += dfs(y, x)

    dp[i][j] = ways
    return dp[i][j]

print(dfs(0, 0))