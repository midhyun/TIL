import sys
from heapq import heappop, heappush
sys.stdin = open('14948_군대탈출하기.txt')
input = sys.stdin.readline

INF = sys.maxsize
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(n)]
visited = [[[INF]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = graph[0][0]
start = []
start.append((graph[0][0], 0, 0, 0))

while start:
    step, i, j, cnt = heappop(start)
    temp = visited[i][j][cnt]
    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]
        if 0 <= y < n and 0 <= x < m:
            n_step = max(graph[y][x], temp)
            if visited[y][x][cnt] > n_step:
                visited[y][x][cnt] = n_step
                heappush(start, (n_step, y, x, cnt))
        if not cnt:
            y = y + dy[k]
            x = x + dx[k]
            if 0 <= y < n and 0 <= x < m:
                n_step = max(graph[y][x], temp)
                if visited[y][x][cnt+1] > n_step:
                    visited[y][x][cnt+1] = n_step
                    heappush(start, (n_step, y, x, cnt+1))

print(min(visited[n-1][m-1]))
