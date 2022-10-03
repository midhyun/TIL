import sys
from collections import deque
from itertools import combinations
sys.stdin = open('16988_baduk2.txt')
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True
    flag = True
    cnt = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < m and 0 <= y < n and not visited[y][x]:
                if graph[y][x] == 2:
                    cnt += 1
                    visited[y][x] = True
                    q.append((y, x))
                elif graph[y][x] == 0:
                    flag = False
    if not flag:
        return 0
    return cnt

n, m = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(n)]
positions = []

for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            positions.append((i, j))

combies = list(combinations(positions, 2))

result = 0
for combi in combies:
    for com in combi:
        graph[com[0]][com[1]] = 1
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2 and not visited[i][j]:
                cnt += bfs(i, j)
    result = max(cnt, result)
    for com in combi:
        graph[com[0]][com[1]] = 0

print(result)