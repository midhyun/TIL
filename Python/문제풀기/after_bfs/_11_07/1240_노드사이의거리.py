import sys
sys.stdin = open('1240_노드사이의거리.txt')
input = sys.stdin.readline
def dfs(x, d):
    if not visited[x]:
        visited[x] = True
        for grap in graph[x]:
            dist[grap[0]] = d + grap[1]
            if grap[0] == e:
                return
            dfs(grap[0], d+grap[1])

n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
for _ in range(m):
    s, e = map(int, input().split())
    visited = [False] *(n+1)
    dist = [0]*(n+1)
    dfs(s, 0)
    print(dist[e])