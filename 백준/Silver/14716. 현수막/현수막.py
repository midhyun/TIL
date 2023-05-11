import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
dx, dy = [0, 0, -1, 1, -1, 1, -1, 1], [-1, 1, 0, 0, -1, 1, 1, -1]
visited = [[False]*M for _ in range(N)]
def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        i, j = q.popleft()
        for k in range(8):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < N and 0 <= x < M and not visited[y][x] and matrix[y][x]:
                visited[y][x] = True
                matrix[y][x] = 0
                q.append((y, x))

cnt = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j]:
            bfs(i, j)
            cnt += 1

print(cnt)