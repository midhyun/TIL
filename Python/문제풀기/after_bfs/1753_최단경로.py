import sys
import heapq
sys.stdin = open('1753_최단경로.txt')
input = sys.stdin.readline

V, E = map(int, input().split()) # 노드 개수, 간선 개수
K = int(input()) # 시작점
INF = 1e9
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
# < 반복문 >    
# visited = [False] * (V+1)
# def gsn():
#     min_value = INF
#     index = 0 # 최단 거리가 가장 짧은 노드 (인덱스)
#     for i in range(1, V+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for _ in range(V - 1):
#         now = gsn()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
# < 우선순위 큐 >
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

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])