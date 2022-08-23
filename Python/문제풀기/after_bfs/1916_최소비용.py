import sys
import heapq
sys.stdin = open('1916_최소비용.txt')
input = sys.stdin.readline
INF = 1e9
N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(N+1):
    if i == end:
        print(distance[i])