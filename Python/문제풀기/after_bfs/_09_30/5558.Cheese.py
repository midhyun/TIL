import sys
from collections import deque
import copy
sys.stdin = open('5558.Cheese.txt')
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph_origin = [[i for i in input().strip()] for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(start, goal):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < m and 0 <= y < n and not visited[y][x] and graph[y][x] != 'X':
                visited[y][x] = True
                if graph_origin[y][x] == goal:
                    graph[y][x] = graph[i][j] + 1
                    return (y, x, graph[y][x])
                graph[y][x] = graph[i][j] + 1
                q.append((y, x))

start = ()
factories = [0]*(k+1)
for i in range(n):
    for j in range(m):
        if graph_origin[i][j] == 'S':
            graph = copy.deepcopy(graph_origin)
            graph[i][j] = 0
            start = (i, j)
            for i in range(1, k+1):
                visited = [[False]*m for _ in range(n)]
                y, x, dis = bfs(start, str(i))
                start = (y, x)
            break
print(dis)