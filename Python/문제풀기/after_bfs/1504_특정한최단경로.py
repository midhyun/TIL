import sys
import heapq
sys.stdin = open('1504_특정한최단경로.txt')
input = sys.stdin.readline
INF = 1e9
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

u, v = map(int, input().split())
lst = [u, v]
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if dist < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
result = 0
lst = [1,u,v,N]
for i in range(3):
    distance = [INF] * (N+1)
    dijkstra(lst[i])
    if distance[lst[i]] == INF:
        result = -1
        break
    else:
        result += distance[lst[i+1]]

print(result)