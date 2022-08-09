import sys
sys.stdin = open('무방향그래프.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]
lst = [[] for _ in range(N+1)]

for idx in range(1, M+1):
    i, j = map(int, input().split())
    matrix[i][j] = 1
    matrix[j][i] = 1
    lst[i].append(j)
    lst[j].append(i)
print(matrix)
print(lst)