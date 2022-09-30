import sys
from collections import deque
sys.stdin = open('2589_보물섬.txt')
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < m and 0 <= y < n and graph[y][x] == 'L' and visited[y][x] == -1:
                visited[y][x] = visited[i][j] + 1
                q.append((y, x))

n, m = map(int, input().split())
graph = [[i for i in input().strip()] for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[-1]*m for _ in range(n)]
            temp = 0
            bfs(i, j)
            for visit in visited:
                temp = max(temp, max(visit))
            result = max(temp, result)

print(result)