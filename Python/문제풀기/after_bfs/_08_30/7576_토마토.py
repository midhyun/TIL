import sys
from collections import deque
sys.stdin = open('7576_토마토.txt')
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < M and 0 <= y < N:
                if tomato[y][x] == 0:
                    tomato[y][x] = tomato[i][j] + 1
                    queue.append((y, x))
result = 0

bfs()

for i in tomato:
    if 0 in i:
        result = 0
        break
    else:
        result = max(result, max(i))

print(result - 1)