import sys
input = sys.stdin.readline

def solution_dp():
    N, M = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(N)]
    dp = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if j == 0:
                dp[i][j] = graph[i][j] + dp[i-1][j]
            else:
                dp[i][j] = graph[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    print(dp[N-1][M-1])

solution_dp()