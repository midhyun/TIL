import sys
from collections import deque
from itertools import combinations
import copy
sys.stdin = open('17141_연구소2.txt')
input = sys.stdin.readline

def bfs(com):
    q = deque()
    for k in com:
        q.append(k)
        visited[k[0]][k[1]] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < n and 0 <= y < n:
                if not visited[y][x] and graph[y][x] == 0:
                    visited[y][x] = True
                    graph[y][x] = graph[i][j] + 1
                    q.append((y, x))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
n, m = map(int, input().split())
temp_g = [[*map(int, input().split())] for _ in range(n)]
viruses = []
for i in range(n):
    for j in range(n):
        if temp_g[i][j] == 2:
            temp_g[i][j] = 0
            viruses.append((i, j))
        if temp_g[i][j] == 1:
            temp_g[i][j] = -1

virus = combinations(viruses, m)
result = 1e9
for combi in virus:
    visited = [[False]*n for _ in range(n)]
    graph = copy.deepcopy(temp_g)
    bfs(combi)
    temp = 0
    flag = 0
    for i in graph:
        flag += i.count(0)
        temp = max(max(i),temp)
    if flag == m:
        result = min(temp, result)

if result == 1e9:
    print(-1)
else:
    print(result)