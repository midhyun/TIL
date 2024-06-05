import sys
from heapq import heappush, heappop
input = sys.stdin.readline

INF = sys.maxsize
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dist = [INF] * (N + 1)
visited = [False] * (N + 1)
total_cost = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    heappush(graph[A], (C, B))
    heappush(graph[B], (C, A))
    total_cost += C

def solution():
    dist[1] = 0
    answer = 0
    cnt = 0
    heap = [(0, 1)]
    while heap:
        if cnt == N:
            break

        cost, node = heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        answer += cost
        cnt += 1
        for c, n in graph[node]:
            if not visited[n]:
                heappush(heap, (c, n))
    if cnt != N:
        return -1

    return total_cost-answer

print(solution())