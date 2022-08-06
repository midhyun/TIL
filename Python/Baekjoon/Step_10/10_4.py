# 체스판 칠하기
import sys
sys.stdin = open('10_4.txt')
input = sys.stdin.readline
from pprint import pprint

N, M = map(int, input().split())
board_nm = [ [_ for _ in input().strip()] for i in range(N)]
cnt_lst = []

for i in range(N-7):    # 9
    for j in range(M-7):# 23 
        cnt = 0
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0 and board_nm[i+y][j+x] != 'W':
                    cnt += 1
                elif (x + y) % 2 != 0 and board_nm[i+y][j+x] != 'B':
                    cnt += 1
        cnt_lst.append(cnt)
        cnt = 0
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0 and board_nm[i+y][j+x] != 'B':
                    cnt += 1
                elif (x + y) % 2 != 0 and board_nm[i+y][j+x] != 'W':
                    cnt += 1
        cnt_lst.append(cnt)
print(min(cnt_lst))