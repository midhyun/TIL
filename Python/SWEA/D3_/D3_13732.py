from ast import Pass
import sys
sys.stdin = open('input.txt','r')

T = int(input())
def check(board, cnt, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                sero = 0
                garo = 0
                for k in range(i+1,N):
                    if board[k][j] == 1:
                        sero += 1
                    else :
                        break
                
                for k in range(j+1,N):
                    if board[i][k] == 1:
                        garo += 1
                    else : break
                if garo != sero:
                    return 'no'

                for x in range(i, i+sero+1):
                    for y in range(j, j+garo+1):
                        if board[x][y] == 1:
                            cnt -= 1
                        else :
                            result = 'no'
                if cnt !=0 :
                    return 'no'
                return 'yes'
for test_case in range(1, T + 1):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    e_num = []
    cnt = 0
    result = 'no'
    for i in range(N):
        info = list(map(str, input()))
        for j in range(N):
            if info[j] == '#':
                board[i][j] = 1
                cnt += 1
            else:
                continue


    print(f'#{test_case} {check(board, cnt, N)}')