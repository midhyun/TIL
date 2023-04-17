import sys
input = sys.stdin .readline

def solution():

    for i in range(1, N+1):
        for j in range(M):
            if j < M-1:
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + matrix[i-1][j]
            if 0 < j:
                dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + matrix[i-1][j]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + matrix[i-1][j]

    result = INF
    for values in dp[-1]:
        result = min(result, min(values))

    return result

N, M = map(int, input().split())
INF = sys.maxsize
matrix = [[*map(int, input().split())] for _ in range(N)]
dp =[[[0,0,0] for _ in range(M)]] + [[[INF,INF,INF] for _ in range(M)] for _ in range(N)]

print(solution())