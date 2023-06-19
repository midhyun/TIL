import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

YES = 1
NO = 0
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
dp = [[0]*(N+1) for _ in range(2)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(root):
    visited[root] = True
    dp[YES][root] = 1

    for child in graph[root]:
        if visited[child]: continue
        dfs(child)

        dp[YES][root] += min(dp[YES][child], dp[NO][child])
        dp[NO][root] += dp[YES][child]

dfs(1)

print(min(dp[YES][1], dp[NO][1]))