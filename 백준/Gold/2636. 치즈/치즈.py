import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(i, j):
    visited = [[False]*M for _ in range(N)]
    visited[i][j] = True
    q = deque()
    cnt = 0
    q.append((i, j))
    while q:
        i, j = q.popleft()

        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= x < M and 0 <= y < N:
                if not visited[y][x]:
                    if not matrix[y][x]:
                        visited[y][x] = True
                        check[y][x] = True
                        q.append((y, x))
                    elif matrix[y][x]:
                        cnt += 1
                        visited[y][x] = True
                        matrix[y][x] = 0
    return cnt
check = [[False]*M for _ in range(N)]
result, last_cheese = 0, []

for i in range(N):
    for j in range(M):
        if not matrix[i][j] and not check[i][j]:
            result += 1
            last_cheese.append(bfs(i, j))

print(result-1, last_cheese[-2], sep='\n')