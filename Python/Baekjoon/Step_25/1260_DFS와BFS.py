import sys
from collections import deque
sys.stdin = open('1260_DFS와BFS.txt')
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x, visit_dfs = []):
    visited_dfs[x] = True
    visit_dfs.append(x)
    graph[x] = sorted(graph[x])
    for i in graph[x]:
        if not visited_dfs[i]:
            dfs(i)
    return visit_dfs

visit_dfs = dfs(r)
visit_bfs = []
q = deque()
q.append(r)
visited_bfs[r] = True
while q:
    cur = q.popleft()
    visit_bfs.append(cur)
    graph[cur] = sorted(graph[cur])
    for i in graph[cur]:
        if not visited_bfs[i]:
            q.append(i)
            visited_bfs[i] = True

for i in visit_dfs:
    print(i, end=' ')
print()
for i in visit_bfs:
    print(i, end=' ')