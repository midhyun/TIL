import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('3025_돌던지기.txt')
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    throw_cnt = int(input())
    stack = [[] for _ in range(M)]

    def MoveStone(i, j, stackNum):
        stack[stackNum].append((i, j))
        if i == N-1 or board[i+1][j] == 'X':
            stack[stackNum].pop()
            board[i][j] = 'O'
            return
        if board[i+1][j] == '.':
            MoveStone(i+1, j, stackNum)
        elif board[i+1][j] == 'O':
            if 0 < j and i < N-1 and board[i][j-1] == '.' and board[i+1][j-1] == '.':
                MoveStone(i+1, j-1, stackNum)
            elif j < M -1 and i < N-1 and board[i][j+1] == '.' and board[i+1][j+1] == '.':
                MoveStone(i+1, j+1, stackNum)
            else:
                stack[stackNum].pop()
                board[i][j] = 'O'
                return

    for _ in range(throw_cnt):
        j = int(input()) - 1
        while stack[j]:
            x, y = stack[j][-1]
            if board[x][y] == '.':
                break
            stack[j].pop()
        
        if stack[j]:
            x, y = stack[j].pop()
            MoveStone(x, y, j)
        else:
            MoveStone(0, j, j)
    

    for b in board:
        print(''.join(b))
    return

solution()
