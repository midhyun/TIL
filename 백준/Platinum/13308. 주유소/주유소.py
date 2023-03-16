import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())
costs = [0] + [*map(int, input().split())]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
visited = [[False]* (2501) for _ in range(N+1)]

def dijkstra():
    q = []
    heappush(q, (1, costs[1], 0))
    while q:
        cur, cost, dist = heappop(q)
        if visited[cur][cost]: continue
        if cur == N: return dist

        visited[cur][cost] = True
        for nxt in graph[cur]:
            heappush(q, (nxt[0], min(cost, costs[nxt[0]]), cost*nxt[1] + dist))

print(dijkstra())