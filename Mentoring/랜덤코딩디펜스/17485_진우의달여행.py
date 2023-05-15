import sys
sys.stdin = open('17485_진우의달여행.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
INF = sys.maxsize
matrix = [[*map(int, input().split())] for _ in range(N)]
dp = [[[0]*3 for _ in range(M)]] + [[[INF]*3 for _ in range(M)] for _ in range(N)]

for i in range(1, N+1):
    for j in range(M):
        if j > 0:
            dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + matrix[i-1][j]

        if j < M-1:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + matrix[i-1][j]

        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + matrix[i-1][j]

result = INF
for i in range(M):
    for j in range(3):
        result = min(dp[-1][i][j], result)

print(result)