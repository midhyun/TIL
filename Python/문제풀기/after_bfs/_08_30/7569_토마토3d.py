from hmac import digest_size
import sys
from collections import deque
sys.stdin = open('7569_토마토3d.txt')
input = sys.stdin.readline

M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque()
dz = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dx = [0,0,0,0,1,-1]

for h in range(H):
    for i in range(N):
        for j in range(M):
            if boxes[h][i][j] == 1:
                queue.append((h, i, j))

def bfs():
    while queue:
        h, i, j = queue.popleft()
        for k in range(6):
            z = h + dz[k]
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= z < H and 0 <= y < N and 0 <= x < M:
                if boxes[z][y][x] == 0:
                    boxes[z][y][x] = boxes[h][i][j] + 1
                    queue.append((z, y, x))

bfs()
result = 0
check = True
for h in boxes: # i = 2차원 리스트
    for i in h: # j = 1차원 리스트
        if 0 in i:
            check = False
            break
        else:
            result = max(result, max(i))

if not check:
    print(-1)
else:
    print(result -1)