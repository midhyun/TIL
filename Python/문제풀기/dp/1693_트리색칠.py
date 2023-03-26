import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('1693_트리색칠.txt')
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
dp = [[0]*(n+1) for _ in range(2)]

def dfs(u):
    visited[u] = True
    dp[0][u] = dp[1][u] = 1
    
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
            dp[0][u] += dp[1][v]
            dp[1][u] += min(dp[0][v], dp[1][v])

dfs(1)
print(min(dp[0][1], dp[1][1]))
print(dp)