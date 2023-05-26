import sys
sys.stdin = open('1967_트리의지름.txt')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(visited, cur, d):
    res = 0
    for nxt, dist in graph[cur]:
        if visited[nxt] == -1:
            visited[nxt] = d + dist
            res = max(res, dfs(visited, nxt, d + dist) + dist)
    
    return res

result = 0
visited = [-1]*(N+1)
visited[1] = 0
dfs(visited, 1, 0)

s_node = visited.index(max(visited))
visited = [-1]*(N+1)
visited[s_node] = 0
dfs(visited, s_node, 0)

print(max(visited))