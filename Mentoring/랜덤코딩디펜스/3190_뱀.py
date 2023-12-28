import sys
from collections import deque
sys.stdin = open('3190_뱀.txt')
input = sys.stdin.readline

def solution():
    N = int(input()) # 보드의 크기
    K = int(input()) # 사과의 개수
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # 우 하 좌 상
    board = [[0]*N for _ in range(N)]
    dir = 0 # 뱀의 방향
    board[0][0] = 1 # 초기 뱀
    time = 0
    snake = deque()
    snake.append((0, 0)) # 현재 뱀이 있는 board

    for _ in range(K):
        i, j = map(int, input().split())
        board[i-1][j-1] = 2 # 사과
    
    L = int(input()) # 뱀의 방향 변환 횟수
    turn_snake = []
    for _ in range(L):
        X, C = input().split() # L 왼쪽 D 오른쪽
        turn_snake.append((int(X), C))

    turn_cnt = 0
    while True:
        time += 1
        i, j = snake[-1] # 뱀의 머리
        ni, nj = i + dy[dir], j + dx[dir] # 이동 후 뱀의 머리
        if turn_cnt < L and turn_snake[turn_cnt][0] == time:
            X, C = turn_snake[turn_cnt]
            turn_cnt += 1
            if C == 'D':
                dir += 1
                dir %= 4
            if C == 'L':
                dir -= 1
                dir %= 4

        if 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj] == 1:
                return time
            if board[ni][nj] == 2:
                board[ni][nj] = 1
                snake.append((ni, nj))
                continue
            if board[ni][nj] == 0:
                board[ni][nj] = 1
                snake.append((ni, nj))
                li, lj = snake.popleft()
                board[li][lj] = 0
        else:
            return time
        
print(solution())