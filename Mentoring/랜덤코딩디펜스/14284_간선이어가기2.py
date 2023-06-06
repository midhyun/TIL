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

def dijkstra(s, d):
    visited = [INF]*(N+1)
    q = []
    heappush(q, (d, s))
    visited[s] = 0
    while q:
        d, cur = heappop(q)
        if cur == T:
            return d
        for nxt, cost in graph[cur]:
            heappush(q, (d + cost, nxt))
            
print(dijkstra(S, 0))