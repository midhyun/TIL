import sys
sys.stdin = open('1236.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]
cnt_n = 0
cnt_m = 0

for i in range(n):                                  # 공백 행 카운트
    if matrix[i] == ['.']*m:
        cnt_n += 1

for i in range(m):                                  # 공백 열 카운트
    if [matrix[j][i] for j in range(n)] == ['.']*n:
        cnt_m += 1

print(max(cnt_n,cnt_m))
