import sys
from collections import deque
sys.stdin = open('10026_적록색약.txt')
input = sys.stdin.readline

# NxN 그래프 (R, G, B)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
graph = [[i for i in input().strip()] for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def bfs(s):
    q = deque()
    q.append(s)
    visited[s[0]][s[1]] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < n and 0 <= y < n and not visited[y][x]:
                if graph[i][j] == graph[y][x]:
                    visited[y][x] = True
                    q.append((y, x))

cnt_normal = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs((i, j))
            cnt_normal += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False]*n for _ in range(n)]
cnt_cb = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs((i, j))
            cnt_cb += 1

print(cnt_normal, cnt_cb)