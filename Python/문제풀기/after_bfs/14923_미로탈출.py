import sys
from collections import deque
sys.stdin = open('14923_미로탈출.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
sy, sx = map(int, input().split())
ey, ex = map(int, input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1
graph = [[*map(int, input().split())] for _ in range(n)]
visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(starty,startx, check):
    q = deque()
    q.append((starty, startx, check))
    visited[starty][startx] = [0, 0]
    while q:
        i, j, check = q.popleft()
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < n and 0 <= x < m:
                if check == 1 and graph[y][x] == 1:
                    visited[y][x][0] = visited[i][j][1] + 1
                    q.append((y, x, 0))
                elif visited[y][x][check] == -1 and graph[y][x] == 0:
                    visited[y][x][check] = visited[i][j][check] + 1
                    q.append((y, x, check))
    return -1
bfs(sy, sx, 1)
if max(visited[ey][ex]) == -1 :
    print(-1)
else:
    print(min(visited[ey][ex]))
