import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
dp = [[0] * 17 for _ in range(n + 1)]
visited = [False] * (n + 1)
def dfs(idx):
    for i in graph[idx]:
        if visited[i]:
            continue
        visited[i] = True
        dfs(i)
        for j in range(1, 17):
            m_num = 100000000
            for k in range(1, 17):
                if j != k:
                    if m_num > dp[i][k]:
                        m_num = dp[i][k]
            dp[idx][j] += m_num
    for i in range(1, 17):
        dp[idx][i] += i

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[1] = True
dfs(1)
print(min(dp[1][1:]))