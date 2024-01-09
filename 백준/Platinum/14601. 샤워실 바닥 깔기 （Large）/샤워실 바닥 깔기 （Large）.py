import sys
input = sys.stdin.readline

def check(y, x, size):
    for i in range(y, y+size):
        for j in range(x, x+size):
            if board[i][j] != 0:
                return False
    return True

def solution(r, c, size):
    global id
    size = size >> 1
    if check(r, c, size):
        board[r+size-1][c+size-1] = id
    if check(r, c+size, size):
        board[r+size-1][c+size] = id
    if check(r+size, c, size):
        board[r+size][c+size-1] = id
    if check(r+size, c+size, size):
        board[r+size][c+size] = id

    id += 1
    
    if size == 1:
        return

    solution(r, c, size)
    solution(r+size, c, size)
    solution(r, c+size, size)
    solution(r+size, c+size, size)

k = int(input())
x, y = map(int, input().split())
board = [[0]*(1<<k) for _ in range(1<<k)]
board[(1<<k)-y][x-1] = -1

id = 1
solution(0, 0, 1<<k)

for b in board:
    print(*b)