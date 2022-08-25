import sys
sys.stdin = open('2116_주사위쌓기.txt')
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
# [A5,B3,C4,D1,E2,F1],[AF,BD,CE]
lst = [5,3,4,1,2,0]
answ = 0
for i in range(6):
    result = 0
    down_side = matrix[0][i]
    up_side = matrix[0][lst[i]] # i = 아랫면 lst[i] =윗면
    if (up_side == 6 and down_side == 5) or (up_side == 5 and down_side == 6):
        result += 4
    elif up_side == 6 or down_side == 6:
        result += 5
    else: result += 6
    for j in range(1,n):
        for k in range(6):
            if matrix[j][k] == up_side:
                down_side = matrix[j][k]
                up_side = matrix[j][lst[k]]
                if (up_side == 6 and down_side == 5) or (up_side == 5 and down_side == 6):
                    result += 4
                elif up_side == 6 or down_side == 6:
                    result += 5
                else: result += 6
                break
    if result > answ:
        answ = result
print(answ)