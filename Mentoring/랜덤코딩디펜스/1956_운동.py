import sys
from heapq import heappush, heappop
sys.stdin = open('1956_운동.txt')
input = sys.stdin.readline

V, E = map(int, input().split())
INF = sys.maxsize
matrix = [[] for _ in range(V+1)]
graph = [[INF]*(V+1) for _ in range(V+1)]
q = []
for _ in range(E):
    a, b, c = map(int, input().split())
    matrix[a].append((b, c))
    graph[a][b] = c
    heappush(q, (c, a, b))

while q:
    d, s, e = heappop(q)

    if s == e:
        print(d)
        break

    if graph[s][e] < d:
        continue

    for ng, dist in matrix[e]:
        distance = d + dist
        if distance < graph[s][ng]:
            graph[s][ng] = distance
            heappush(q, (distance, s, ng))
else:
    print(-1)