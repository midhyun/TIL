import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [INF] * (n+1)
q = []
heappush(q, (0, 1))
while q:
    dist, node = heappop(q)
    if dist > visited[node]:
        continue
    for nx, x in graph[node]:
        cost = dist + nx
        if visited[x] > cost:
            visited[x] = cost
            heappush(q, (cost, x))
print(visited[n])