import sys
import heapq
sys.stdin = open('1261_알고스팟.txt')
input = sys.stdin.readline

M, N = map(int, input().split())
INF = 1e9
matrix = [list(input().strip()) for _ in range(N)]
distance = [[INF]*M for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dijkstra(i, j):
    q = []
    heapq.heappush(q, (0, i, j))
    distance[i][j] = 0
    while q:
        dist, i, j = heapq.heappop(q)            # now = (i, j)
        if distance[i][j] < dist:
            continue
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= x < M and 0 <= y < N:
                cost = dist + int(matrix[y][x])
                if cost < distance[y][x]:
                    distance[y][x] = cost
                    heapq.heappush(q, (cost, y, x))

dijkstra(0,0)
print(distance[N-1][M-1])