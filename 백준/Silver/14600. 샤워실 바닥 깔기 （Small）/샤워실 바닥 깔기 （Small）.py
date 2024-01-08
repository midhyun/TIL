import sys
input = sys.stdin.readline

def check(y, x, size):
    for i in range(y, y + size):
        for j in range(x, x + size):
            if matrix[i][j] != 0:
                return False
    return True

def solution(y, x, size):
    global id

    size = size >> 1
    if check(y, x, size):
        matrix[y+size-1][x+size-1] = id
    if check(y + size, x, size):
        matrix[y+size][x+size-1] = id
    if check(y + size, x + size, size):
        matrix[y+size][x+size] = id
    if check(y, x + size, size):
        matrix[y+size-1][x+size] = id

    id += 1

    if size == 1:
        return
    
    solution(y, x, size)
    solution(y+size, x, size)
    solution(y, x+size, size)
    solution(y+size, x+size, size)

k = int(input())
x, y = map(int, input().split())
matrix = [[0]*(1<<k) for _ in range(1<<k)]
matrix[(1 << k) - y][x-1] = -1

id = 1

solution(0, 0, 1 << k)
for m in matrix:
    print(*m)