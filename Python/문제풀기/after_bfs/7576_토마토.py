import sys
sys.stdin = open('7576_토마토.txt')
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0
while True:

    check = False
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                visited[i][j] = True
                for k in range(4):
                    x = j + dx[k]
                    y = i + dy[k]
                    if 0 <= x < M and 0 <= y < N:
                        if tomato[y][x] == 0:
                            visited[y][x] =True
                            check = True
    for i in range(N):
        for j in range(M):
            if visited[i][j] == True:
                tomato[i][j] = 1
    if not check:
        break

    cnt += 1

for i in range(N):
    if 0 in tomato[i]:
        cnt = -1

print(cnt)
