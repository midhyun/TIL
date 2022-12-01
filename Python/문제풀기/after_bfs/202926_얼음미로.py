import sys
from collections import deque
sys.stdin = open('202926_얼음미로.txt')
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
start = []
end = []
dx, dy = [0,0,-1,1], [-1,1,0,0]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'T':
            start = (i, j)
        if graph[i][j] == 'E':
            end = (i, j)
            
visited[end[0]][end[1]] = int(1e9)
visited[start[0]][start[1]] = 0
graph[start[0]][start[1]] = 0
q = deque()
q.append(start)
while q:
    i, j= q.popleft()
    for k in range(4):
        y, x = i+dy[k], j+dx[k]
        temp = visited[i][j]
        while True:
            if 0 <= y < n and 0 <= x < m:
                if graph[y][x] == 'H':
                    break
                if graph[y][x] == 'E':
                    visited[y][x] = min(temp, visited[y][x])
                    break
                if graph[y][x] == 'R':
                    if (visited[y-dy[k]][x-dx[k]] == -1 or visited[y-dy[k]][x-dx[k]] > temp) and (i != y-dy[k] or j != x-dx[k]):
                        visited[y-dy[k]][x-dx[k]] = temp
                        q.append((y-dy[k], x-dx[k]))
                        break
                    else:
                        break
                temp += int(graph[y][x])
                y, x = y+dy[k], x+dx[k]
            else:
                break

if visited[end[0]][end[1]] == int(1e9):
    print(-1)
else:
    print(visited[end[0]][end[1]])