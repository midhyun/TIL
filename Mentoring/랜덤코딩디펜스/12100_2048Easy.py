import sys
import copy
sys.stdin = open('12100_2048Easy.txt')
input = sys.stdin.readline

def solution():
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
    def move(direction, board, cnt):
        if cnt == 5:
            return max([max(i) for i in board])
        
        check = [[False] * N for _ in range(N)]
        for _ in range(direction):
            temp = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    temp[j][N-1-i] = board[i][j]
            board = temp

        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    continue
                y, x = i, j
                while y > 0:
                    y -= 1
                    if board[y][x] == 0:
                        board[y][x] = board[y+1][x]
                        board[y+1][x] = 0
                        y, x = y, x
                    elif board[y][x] == board[y+1][x] and not check[y][x]:
                        board[y][x] *= 2
                        board[y+1][x] = 0
                        check[y][x] = True
                        break
                    else:
                        break

        a = move(0, copy.deepcopy(board), cnt+1)
        b = move(1, copy.deepcopy(board), cnt+1)
        c = move(2, copy.deepcopy(board), cnt+1)
        d = move(3, copy.deepcopy(board), cnt+1)

        return max(a, b, c, d)

    N = int(input())
    board = [[*map(int, input().split())] for _ in range(N)]
    
    a = move(0, copy.deepcopy(board), 0)
    b = move(1, copy.deepcopy(board), 0)
    c = move(2, copy.deepcopy(board), 0)
    d = move(3, copy.deepcopy(board), 0)

    print(max(a, b, c, d))

max_block = 0
def another_sol():
    def rotate(board):
        return [[board[n-1-j][i] for j in range(n)] for i in range(n)]


    def slide(line):
        merged = [x for x in line if x != 0]
        for i in range(1, len(merged)):
            if merged[i-1] == merged[i]:
                merged[i-1], merged[i] = merged[i-1]*2, 0
        res = [x for x in merged if x]
        return res + [0]*(n - len(res))


    def dfs(lvl, board):
        global max_block
        if lvl == 5:
            max_block = max(max_block, max(map(max, board)))
            return
        for _ in range(4):
            slided = [slide(row) for row in board]
            if slided != board:
                dfs(lvl+1, slided)
            board = rotate(board)


    n = int(input())
    init = [list(map(int, input().split())) for _ in range(n)]

    max_block = 0
    dfs(0, init)

    print(max_block if n != 1 else init[0][0])

another_sol()