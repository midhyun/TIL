import sys
import heapq
sys.stdin = open('1238_파티.txt')
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [0] + [[] for _ in range(n)]
INF = 1e9
for i in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

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

result = []
for i in range(1,n+1):
    temp = 0
    distance = [INF]*(n+1)
    dijkstra(i)
    temp += distance[x]
    distance = [INF]*(n+1)
    dijkstra(x)
    temp += distance[i]
    result.append(temp)
print(max(result))