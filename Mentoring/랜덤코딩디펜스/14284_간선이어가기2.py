import sys
from heapq import heappop, heappush
sys.stdin = open('14284_간선이어가기2.txt')
input = sys.stdin.readline

INF = sys.maxsize
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
S, T = map(int, input().split())
# 다익스트라 종료조건 부여
def dijkstra(s, d):
    visited = [INF]*(N+1)
    q = []
    heappush(q, (d, s))
    while q:
        d, cur = heappop(q)
        if cur == T:
            return d
        for nxt, cost in graph[cur]:
            dist = d + cost
            if dist < visited[nxt]:
                visited[nxt] = dist
                heappush(q, (dist, nxt))

print(dijkstra(S, 0))

# 다익스트라 종료조건 미부여
def dijkstra1(s, d):
    visited = [INF]*(N+1)
    q = []
    heappush(q, (d, s))
    visited[s] = 0
    while q:
        d, cur = heappop(q)
        for nxt, cost in graph[cur]:
            dist = visited[cur] + cost
            if dist < visited[nxt]:
                visited[nxt] = dist
                heappush(q, (cost, nxt))
    return visited[T]

print(dijkstra1(S, 0))