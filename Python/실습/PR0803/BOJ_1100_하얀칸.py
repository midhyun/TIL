# 8x8 체스판 에서 하얀칸에 있는 말의 갯수

import sys
sys.stdin = open('1100.txt')
input = sys.stdin.readline

chess_board = [list(input()) for _ in range(8)]             # 체스판 배열 8 x 8
cnt = 0
for i in range(8):                                          # 각 칸의 인덱스값의 합이 짝수인 경우 하얀 칸
    for j in range(8):
        if (i + j) % 2 == 0 and chess_board[i][j] == 'F':   # 하얀칸에 'F' 일 경우 cnt += 1
            cnt += 1
print(cnt)