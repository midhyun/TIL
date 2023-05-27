import sys
sys.stdin = open('21922_학부연구생민상.txt')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
visited = [[[0]*4 for _ in range(M)] for _ in range(N)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
# 홀수: x축이동, 짝수: y축이동 [상, 좌, 하, 우]

def find_start():
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 9:
                visited[i][j] = [1, 1, 1, 1]
                for k in range(4):
                    wind(k, (i, j))


def wind(dir, cur):
    i, j = cur
    y, x = i + dy[dir], j + dx[dir]

    if 0 <= y < N and 0 <= x < M and not visited[y][x][dir]:
        if matrix[y][x] == 9:
            return
        visited[y][x][dir] = 1
        if dir % 2 == 0:
            if matrix[y][x] == 2:
                return
            elif matrix[y][x] == 3:
                dir -= 1
            elif matrix[y][x] == 4:
                dir += 1
        elif dir % 2 == 1:
            if matrix[y][x] == 1:
                return
            elif matrix[y][x] == 3:
                dir += 1
            elif matrix[y][x] == 4:
                dir -= 1

        wind(dir%4, (y, x))


start = find_start()

result = 0
for i in range(N):
    for j in range(M):
        if 1 in visited[i][j]:
            result += 1
print(result)