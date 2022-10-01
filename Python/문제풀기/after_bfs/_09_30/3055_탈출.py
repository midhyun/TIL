import sys
from collections import deque
sys.stdin = open('3055_탈출.txt')
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[i for i in input().strip()]for _ in range(n)]

visited = [[False]*m for _ in range(n)]
goal = []
start = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'D':
            goal = (i, j)
        elif graph[i][j] == '*':
            start.append((1, i, j))
        elif graph[i][j] == 'S':
            start.append((0, i, j))
            graph[i][j] = 0
start.sort(key=lambda x: x[0])
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs():
    q = deque()
    for i in start:
        q.append((i[1],i[2]))
    while q:
        i, j = q.popleft()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < m and 0 <= y < n and graph[y][x] != 'X':
                if graph[i][j] == '*':
                    if not graph[y][x] == '*' and not graph[y][x] == 'D':
                        graph[y][x] = '*'
                        visited[y][x] = True
                        q.append((y, x))
                elif not visited[y][x]:
                    if graph[y][x] == 'D':
                        graph[y][x] = graph[i][j] + 1
                        return graph[goal[0]][goal[1]]
                    graph[y][x] = graph[i][j] + 1
                    visited[y][x] = True
                    q.append((y, x))

    return graph[goal[0]][goal[1]]

result = bfs()
if result == 'D':
    print('KAKTUS')
else:
    print(result)
