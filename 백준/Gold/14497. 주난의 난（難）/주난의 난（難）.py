import sys
from heapq import heappop, heappush
input = sys.stdin.readline

INF = 600
N, M = map(int, input().split())
sy, sx, ey, ex = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[INF]*M for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
sx -= 1; sy -= 1; ex -= 1; ey -= 1; 

def dijkstra(sy, sx):
    q = []
    heappush(q, (0, sy, sx))
    visited[sy][sx] = 0
    while q:
        cost, i, j = heappop(q)
        
        if cost > visited[i][j]: continue
        if i == ey and j == ex: print(cost); break

        for k in range(4):
            x, y = j + dx[k], i + dy[k]
            if 0 <= x < M and 0 <= y < N:
                if graph[y][x] == '0':
                    dist = cost
                else:
                    dist = cost + 1

                if visited[y][x] > dist:
                    visited[y][x] = dist
                    heappush(q, (dist, y, x))

dijkstra(sy, sx)