import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(i, j, info):
    q = deque()
    q.append((i, j, info))
    area = 1
    while q:
        i, j, info = q.popleft()
        for k in range(4):
            if not (info & 1<<k):
                y = i + dy[k]
                x = j + dx[k]
                if not visited[y][x]:
                    area += 1
                    visited[y][x] = cnt
                    q.append((y, x, graph[y][x]))
    return area

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(M)]
visited = [[0]*N for _ in range(M)]
cnt = 0
area = []

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            cnt += 1
            visited[i][j] = cnt
            area.append(bfs(i, j, graph[i][j]))

print(len(area))
print(max(area))

result = 0
for i in range(M):
    for j in range(N):
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= x < N and 0 <= y < M:
                if visited[i][j] != visited[y][x]:
                    result = max(result, area[visited[i][j]-1] + area[visited[y][x]-1])

print(result)