import sys
import heapq
sys.stdin = open('14630_변신로봇.txt')
input = sys.stdin.readline

INF = 1e9
n = int(input())
robots = [input().strip() for i in range(n)]
s, e = map(int, input().split())

graph = [[0]*n for _ in range(n)]
distance = [INF]*n
for i, now in enumerate(robots):
    for j, next in enumerate(robots):
        now = [*map(int, list(now))]
        next = [*map(int, list(next))]
        c = 0
        for k, now_ in enumerate(now):
            c += abs(now_-next[k])**2
        graph[i][j] = c

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i, c in enumerate(graph[now]):
            cost = dist + c
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(s-1)

print(distance[e-1])