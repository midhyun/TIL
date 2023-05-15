import sys
from heapq import heappop, heappush
input = sys.stdin.readline

INF = sys.maxsize
N, M = map(int, input().split())
sight = [*map(int, input().split())]
sight[N-1] = 0
graph = [[] for _ in range(N)]
visited = [INF] * N
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

def solution():
    q = []
    heappush(q, (0, 0))
    while q:
        dist, cur = heappop(q)
        if dist > visited[cur]:
            continue
        
        if cur == N-1:
            return visited[N-1]
            
        for cost, nxt in graph[cur]:
            if sight[nxt]:
                continue

            tmp = cost + dist
            if visited[nxt] > tmp:
                visited[nxt] = tmp
                heappush(q, (tmp, nxt))
    return -1

print(solution())