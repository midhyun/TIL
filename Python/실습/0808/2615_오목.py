import sys
sys.stdin = open('2615.txt')
from pprint import pprint

board = [list(map(int, input().split())) for _ in range(19)]
lst = []
for doll in range(1,3):
    check = False
    for i in range(19):
        for j in range(19):
            if board[i][j] == doll:
                # 가로 
                dx_1 = [1,2,3,4,5,-1]
                dy_1 = [0,0,0,0,0,0]
                cnt = 0
                for k in range(4):
                    x = j + dx_1[k]
                    y = i + dy_1[k]
                    if 0 <= x < 19 and 0 <= y < 19:
                        if board[i][j] == board[y][x]:
                            cnt += 1
                if cnt == 4:
                    check = True
                for k in range(4, 6):
                    x = j + dx_1[k]
                    y = i + dy_1[k]
                    if 0 <= x < 19 and 0 <= y < 19:
                        if board[i][j] == board[y][x]:
                            check = False
                if check == True:
                    lst.append((i+1, j+1))
                    break
                # 대각 하단
                dx_2 = [1,2,3,4,5,-1]
                dy_2 = [1,2,3,4,5,-1]
                cnt = 0
                for k in range(4):
                    x = j + dx_2[k]
                    y = i + dy_2[k]
                    if 0 <= x < 19 and 0 <= y < 19:
                        if board[i][j] == board[y][x]:
                            cnt += 1
                if cnt == 4:
                    check = True
                for k in range(4, 6):
                    x = j + dx_2[k]
                    y = i + dy_2[k]
                    if 0 <= x < 19 and 0 <= y < 19:
                        if board[i][j] == board[y][x]:
                            check = False      
                if check == True:
                    lst.append((i+1, j+1))
                    break
                # 세로
                dx_3 = [0, 0, 0, 0, 0, 0]
                dy_3 = [1, 2, 3, 4, 5, -1]
                cnt = 0
                for k in range(4):
                    x = j + dx_3[k]
                    y = i + dy_3[k]
                    if 0 <= x < 19 and 0 <= y < 19:
                        if board[i][j] == board[y][x]:
                            cnt += 1
                if cnt == 4:
                    check = True
                for k in range(4, 6):
                    x = j + dx_3[k]
                    y = i + dy_3[k]
                    if 0 <= x < 19 and 0 <= y < 19:
                        if board[i][j] == board[y][x]:
                            check = False
                if check == True:
                    lst.append((i+1, j+1))
                    break
                # 대각 상단
                dx_4 = [1,2,3,4,5,-1]
                dy_4 = [-1,-2,-3,-4,-5, 1]
                cnt = 0
                for k in range(4):
                    x = j + dx_4[k]
                    y = i + dy_4[k]
                    if 0 <= x < 19 and 0 <= y < 19:
                        if board[i][j] == board[y][x]:
                            cnt += 1
                if cnt == 4:
                    check = True
                for k in range(4, 6):
                    x = j + dx_4[k]
                    y = i + dy_4[k]
                    if 0 <= x < 19 and 0 <= y < 19:
                        if board[i][j] == board[y][x]:
                            check = False
                if check == True:
                    lst.append((i+1, j+1))
                    break

        if check == True:
            break
    if check == True:
        print(doll)
        print(lst[0][0],lst[0][1])
        break
else: print(0)