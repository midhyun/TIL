import sys
from collections import deque
sys.stdin = open('2146_다리 만들기.txt')
input = sys.stdin.readline

def bfs(a, b, c):
    q = deque()
    q.append((a, b))
    graph[a][b] = c
    visited[a][b] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            y, x = i + dy[k], j + dx[k]
            if 0 <= y < n and 0 <= x < n:
                if not visited[y][x] and graph[y][x] == 1:
                    visited[y][x] = True
                    graph[y][x] = c
                    q.append((y, x))

def bfs_dist(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            y, x = i + dy[k], j + dx[k]
            if 0 <= y < n and 0 <= x < n:
                if not visited[y][x] and graph[y][x] == 0:
                    visited[y][x] = True
                    q.append((y, x))

dx, dy = [0,0,-1,1], [-1,1,0,0]
n = int(input())
graph = [[*map(int, input().split())] for _ in range(n)]

temp = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            visited = [[False]*n for _ in range(n)]
            bfs(i, j, temp)
            temp += 1
            print(i, j)


for i in range(n):
    for j in range(n):
        

for grap in graph:
    print(grap)