# 배열 (i,j) 부터 (x,y)까지 수들의 합.

import sys
sys.stdin = open('2167.txt')
input = sys.stdin.readline

n, m = map(int, input().split())                                # 최대 300 x 300
matrix = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
matrix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        matrix_sum[i][j] = matrix_sum[i][j-1] + matrix[i-1][j-1]

for _ in range(k):                                              # k 는 최대 10000
    i, j, x, y = map(int, input().split())
    result = 0
    for k in range(i, x+1):                                     # 
        result += matrix_sum[k][y] - matrix_sum[k][j-1]
    print(result)