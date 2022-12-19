import sys
from heapq import heappop, heappush
from itertools import permutations
sys.stdin = open('5901_relocation.txt')
input = sys.stdin.readline
INF = int(1e9)
N, M, K = map(int, input().split())
markets = set()
for _ in range(K):
    markets.add(int(input()))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    visited = [INF] * (N+1)
    visited[start] = 0
    while q:
        dist, node = heappop(q)
        if dist > visited[node]:
            continue
        for dx, x in graph[node]:
            cost = dist + dx
            if visited[x] > cost:
                visited[x] = cost
                heappush(q, (cost, x))
    return visited

per = list(permutations(markets, K))
result = INF
visited_list = [0] *(N+1)
for i in markets:
    visited_list[i] = dijkstra(i)

for i in range(1, N+1):
    if i in markets:
        continue
    for permu in per:
        now = i
        temp = 0
        for k, v in enumerate(permu):
            temp += visited_list[v][now]
            now = v

        temp += visited_list[now][i]
        result = min(result, temp)


print(result)