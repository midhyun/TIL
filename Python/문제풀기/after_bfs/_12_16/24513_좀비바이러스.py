import sys
from collections import deque
sys.stdin = open('24513_좀비바이러스.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
q = deque()

a = 0
b = 0
c = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j, 0))
            visited[i][j] = -1
            a += 1
        elif graph[i][j] == 2:
            q.append((i, j, 0))
            visited[i][j] = -1
            b += 1
while q:
    i, j, cnt = q.popleft()
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= y < n and 0 <= x < m:
            if graph[i][j] == 3:
                continue
            elif graph[i][j] == 1:
                if graph[y][x] == 0 and not visited[y][x]:
                    graph[y][x] = 1
                    visited[y][x] = cnt+1
                    q.append((y, x, cnt+1))
                    a+=1
                elif graph[y][x] == 2 and visited[y][x] == cnt+1:
                    graph[y][x] = 3
                    b -= 1
                    c += 1
            elif graph[i][j] == 2:
                if graph[y][x] == 0 and not visited[y][x]:
                    graph[y][x] = 2
                    visited[y][x] = cnt+1
                    q.append((y, x, cnt+1))
                    b += 1
                elif graph[y][x] == 1 and visited[y][x] == cnt+1:
                    graph[y][x] = 3
                    a -= 1
                    c += 1

print(a, b, c)