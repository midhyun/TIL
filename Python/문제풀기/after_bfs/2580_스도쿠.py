import sys
sys.stdin = open('2580_스도쿠.txt')
input = sys.stdin.readline

matrix = [list(map(int, input().split()))for _ in range(9)]
zeroes = [(i, j) for i in range(9) for j in range(9) if matrix[i][j] == 0]
# 빈칸의 좌표들 zeroes
def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9]
    for k in range(9):
        if matrix[i][k] in promising:
            promising.remove(matrix[i][k])
        if matrix[k][j] in promising:
            promising.remove(matrix[k][j])

    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if matrix[p][q] in promising:
                promising.remove(matrix[p][q])
    
    return promising

flag = False # 답이 출력 되었는가 ?
def dfs(x):
    global flag
    if flag:
        return
    
    if x == len(zeroes):
        for row in matrix:
            print(*row)
        flag = True
        return
    else:
        (i, j) = zeroes[x]
        promising = is_promising(i, j)
        for num in promising:
            matrix[i][j] = num  # 유망한 값을 넣고
            dfs(x + 1)          # 재귀 하고
            matrix[i][j] = 0 # 값을 되돌림 (백트래킹)

dfs(0)