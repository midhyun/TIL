# 배열 (i,j) 부터 (x,y)까지 수들의 합.

import sys
sys.stdin = open('2167.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
result = []
for _ in range(1):
    i, j, x, y = map(int, input().split())
    result = matrix[i-1: x][j-1: y]
print(result)