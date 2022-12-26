import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline
dx, dy = [0,0,-1,1], [-1,1,0,0]
n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
matrix = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(4):
            y, x = i + dy[k], j + dx[k]
            if 0 <= y < n and 0 <= x < n:
                if graph[y][x] == '0':
                    matrix[i][j].append((1, y, x))
                else:
                    matrix[i][j].append((0, y, x))

INF = int(1e9)
visited = [[INF]*n for _ in range(n)]
q = []
heappush(q, (0, 0, 0))
visited[0][0] = 0
while q:
    dist, y, x = heappop(q)
    if dist > visited[y][x]:
        continue
    for dx, i, j in matrix[y][x]:
        cost = dist + dx
        if visited[i][j] > cost:
            visited[i][j] = cost
            heappush(q, (cost, i, j))

print(visited[n-1][n-1])