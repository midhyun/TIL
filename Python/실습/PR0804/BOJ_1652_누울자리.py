import sys
sys.stdin = open('1652.txt')
input = sys.stdin.readline

n = int(input())
room_row = [[i for i in input().strip()] for j in range(n)]
room_col = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        room_col[i][j] = room_row[j][i]
# 가로 검사
cnt_row = 0
cnt_col = 0
for i in range(n):
    check = '.'
    cnt = 0
    for j in room_row[i]:               # 가로검사
        if j == check:
            cnt += 1
        elif j != check:
            if cnt >= 2:
                cnt_row += 1
                cnt = 0
            else :
                cnt = 0
    if cnt >= 2:
        cnt_row += 1
        cnt = 0

    for j in room_col[i]:               # 세로검사
        if j == check:
            cnt += 1
        elif j != check:
            if cnt >= 2:
                cnt_col += 1
                cnt = 0
            else :
                cnt = 0
    if cnt >= 2:
        cnt_col += 1
print(cnt_row, cnt_col)