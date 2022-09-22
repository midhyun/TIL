import sys
import copy
from collections import deque
sys.stdin = open('2573_빙산.txt')
sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]
n, m = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(n)]

def bfs(start):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < m and 0 <= y < n and not visited[y][x]:
                if graph_temp[y][x] != 0:
                    visited[y][x] = True
                    q.append((y, x))
years = 0
while True:
    years += 1
    graph_temp = copy.deepcopy(graph)
    ice_mountains = []
    for i in range(1,n-1):
        for j in range(1,m-1):
            if graph[i][j]:
                ice_mountains.append((i, j))
                cnt = 0
                for k in range(4):
                    x = j + dx[k]
                    y = i + dy[k]
                    if 0 <= x < m and 0 <= y < n:
                        if not graph[y][x]:
                            cnt += 1
                graph_temp[i][j] = max(0, graph[i][j] - cnt)
                     
    dummy = 0
    visited = [[False]*m for _ in range(n)]
    for mountain in ice_mountains:
        i, j = mountain
        if graph_temp[i][j] and not visited[i][j]:
            bfs((i, j))
            dummy += 1
            if dummy > 1:
                break

    if dummy > 1:
        break
    elif dummy == 0:
        years = 0
        break
    graph = graph_temp

print(years)