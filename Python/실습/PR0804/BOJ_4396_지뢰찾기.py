import sys
from pprint import pprint
sys.stdin = open('4396.txt')
input = sys.stdin.readline


n = int(input())
mat_cnt = [[0]*(n+2) for i in range(n+2)]                   # 0 매트릭스
mat_mine = [[i for i in input().strip()] for j in range(n)] # 지뢰 매트릭스

for i in range(n):
    for j in range(n):
        if mat_mine[i][j] == '*':
            for y in range(i, i+3):                         # 지뢰 주변 숫자 카운트
                for x in range(j, j+3):
                    mat_cnt[y][x] += 1

mat_open = [[i for i in input().strip()] for j in range(n)] # 열린 칸 매트릭스

bomb = False
for i in range(n):                                          # 카운트한 매트릭스 중 오픈칸만 숫자표시
    for j in range(n):
        if mat_open[i][j] == 'x':
            if mat_mine[i][j] == '*':                       # 오픈한 칸이 폭탄일 경우
                mat_open[i][j] = '*'                        # 폭탄으로 바꾸어 주고
                bomb = True                                 # 폭탄 여부를 True로 바꿈
            else:
                mat_open[i][j] = mat_cnt[i+1][j+1]          # 오픈한 칸이 폭탄이 아닐경우 cnt 매트릭스의 값을 넣어줌.

if bomb == True:                                            # 폭탄을 열었을 경우
    for i in range(n):
        for j in range(n):
            if mat_mine[i][j] == '*':                       # 결과 매트릭스에 폭탄위치마다 폭탄을 넣어줌
                mat_open[i][j] = '*'

for i in mat_open:                                          # 매트릭스의 값을 출력형식에 맞춰서 출력함.
    for j in i:
        print(j,end='')
    print()