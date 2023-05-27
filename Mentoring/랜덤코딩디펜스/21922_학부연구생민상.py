import sys
sys.stdin = open('21922_학부연구생민상.txt')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]
# 홀수: x축이동, 짝수: y축이동 [상, 하, 좌, 우]

def find_start():
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 9:
                visited[i][j] = 1
                for k in range(4):
                    wind(k, i, j)


def wind(dir, i, j):
    ny, nx = dy[dir], dx[dir]
    y, x = i + ny, j + nx
    while 0 <= y < N and 0 <= x < M:
        visited[y][x] = 1

        if matrix[y][x] == 3:
            ny, nx = -nx, -ny
        elif matrix[y][x] == 4:
            ny, nx = nx, ny
        elif (matrix[y][x] == 1 and ny == 0) or (matrix[y][x] == 2 and nx == 0):
            break
        
        y += ny
        x += nx

find_start()

result = 0
for i in range(N):
    result += sum(visited[i])
print(result)