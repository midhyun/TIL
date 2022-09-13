import sys
import copy
from collections import deque
from itertools import combinations
sys.stdin = open('17142_연구소3.txt')
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(com):
    q = deque()
    for z in com:
        q.append(z)
        visited[z[0]][z[1]] = True
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

n, m = map(int, input().split())
temp_graph = [[*map(int, input().split())] for _ in range(n)]
viruses = []
for i in range(n):
    for j in range(n):
        if temp_graph[i][j] == 2:
            temp_graph[i][j] = 0
            viruses.append((i, j))
        elif temp_graph[i][j] == 1:
            temp_graph[i][j] = -2
virus = combinations(viruses, m)
result = 1e9
for combi in virus:
    graph = copy.deepcopy(temp_graph)
    visited = [[False]*n for _ in range(n)]
    bfs(combi)
    inact = set(viruses) - set(combi)
    for i in inact:
        graph[i[0]][i[1]] = -1
    flag = 0
    temp = 0
    for line in graph:
        temp = max(max(line), temp)
        flag += line.count(0)
    if flag == m:
        result = min(temp, result)

if result == 1e9:
    print(-1)
else: print(result)