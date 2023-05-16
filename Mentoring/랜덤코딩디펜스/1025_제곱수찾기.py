import sys
sys.stdin = open('1025_제곱수찾기.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
T = max(N, M)
dx, dy = [0, 0, -1, 1, -1, 1, -1, 1], [-1, 1, 0, 0, -1, 1, 1, -1]

def bfs(i, j):
    temp = -1
    for d in range(8):
        for k in range(1, T):
            for l in range(1, T):
                cur = matrix[i][j]
                y, x = i, j
                while True:
                    y += dy[d]*k
                    x += dx[d]*l
                    if 0 <= y < N and 0 <= x < M:
                        cur += matrix[y][x]
                        tmp = int(cur)
                        if tmp**0.5 == int(tmp**0.5):
                            temp = max(temp, tmp)
                    else:
                        break



    return temp

result = -1
for i in range(N):
    for j in range(M):
        x = int(matrix[i][j])
        if x**0.5 == int(x**0.5):
            result = max(result, x)
        result = max(result, bfs(i, j))

print(result)