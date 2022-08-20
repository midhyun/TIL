import sys
from turtle import pu

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())                    # N x N 크기의 행렬, 길이 K의 문자
    puzzle = [input().split() for _ in range(N)]        # 1 == 빈칸, 0 == 검은칸
    puzzle_row = [[0]*N for _ in range(N)]              # 행,열 전치
    for i in range(N):
        for j in range(N):
            puzzle_row[i][j] = puzzle[j][i]

    cnt = 0
    for row in puzzle:                                  # 행렬에서 가로로 '1'*K 인 문자열을 찾기위해 각 행을 문자열로 바꾸고 
        cnt += ''.join(row).split('0').count('1'*K)     # .join().split('0') 문자열을 '0'을 구분자로 리스트에 담아줌 '1'*K의 갯수를 카운트에 더함
    for row in puzzle_row:
        cnt += ''.join(row).split('0').count('1'*K)
    print(f'#{test_case} {cnt}')