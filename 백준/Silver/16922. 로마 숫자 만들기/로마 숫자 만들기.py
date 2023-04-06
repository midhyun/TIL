import sys
input = sys.stdin.readline

N = int(input())
check = [[0]*(50*N+1) for _ in range(N)]
check[0][1], check[0][5], check[0][10], check[0][50] = 1, 1, 1, 1

for i in range(1, N):
    for j in range(50*N+1):
        if check[i-1][j]:
            check[i][j+1] = 1
            check[i][j+5] = 1
            check[i][j+10] = 1
            check[i][j+50] = 1

print(sum(check[N-1]))