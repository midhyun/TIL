import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('1937_욕심쟁이판다.txt')
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [1,-1,0,0]
n = int(input())
graph = [[*map(int, input().split())] for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
ans = 0
def dfs(i, j):
    if dp[i][j] == -1:
        dp[i][j] = 0
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < n and 0 <= x < n and graph[y][x] > graph[i][j]:
                dp[i][j]  = max(dp[i][j], dfs(y, x))

    return dp[i][j] + 1
        
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))

print(ans)