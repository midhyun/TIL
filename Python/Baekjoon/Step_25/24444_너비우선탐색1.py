import sys
from collections import deque
sys.stdin = open('24444_너비우선탐색1.txt')
input = sys.stdin.readline

n, m, r = map(int ,input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = [0]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = 1
q = deque([])
q.append(r)
visited[r] = True
while q:
    cur = q.popleft()
    result[cur] = cnt
    cnt += 1
    graph[cur] = sorted(graph[cur])
    for i in graph[cur]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
for i in result[1:]:
    print(i)

