import sys
input = sys.stdin.readline

def solution(start, dp):
    for i in range(start, N):
        dp[0][i+1] = min(dp[1][i]+1, dp[2][i]+1)
        if enemies[0][i] + enemies[1][i] <= W: dp[0][i+1] = min(dp[0][i+1], dp[0][i] + 1)
        if i > 0 and enemies[0][i-1] + enemies[0][i] <= W and enemies[1][i-1] + enemies[1][i] <= W: dp[0][i+1] = min(dp[0][i+1], dp[0][i-1] + 2)

        if i < N-1:
            dp[1][i+1] = dp[0][i+1] + 1
            if enemies[0][i+1] + enemies[0][i] <= W: dp[1][i+1] = min(dp[1][i+1], dp[2][i] + 1)

            dp[2][i+1] = dp[0][i+1] + 1
            if enemies[1][i+1] + enemies[1][i] <= W: dp[2][i+1] = min(dp[2][i+1], dp[1][i] + 1)

    return dp

T = int(input())
results = []

for _ in range(T):
    N, W = map(int, input().split()) # N*2 = 전체구역 수, W = 소대인원
    enemies = [[*map(int, input().split())] for _ in range(2)]
    dp = [[0]*(N+1) for _ in range(3)]
    dp[0][0], dp[1][0], dp[2][0] = 0, 1, 1
    
    dp = solution(0, dp)
    res = dp[0][N]

    if N > 1 and enemies[0][0] + enemies[0][N-1] <= W:
        dp[0][1] = 1
        dp[1][1] = 2
        if enemies[1][0] + enemies[1][1] <= W: dp[2][1] = 1
        else: dp[2][1] = 2

        dp = solution(1, dp)
        res = min(res, dp[2][N-1] + 1)
    
    if N > 1 and enemies[1][0] + enemies[1][N-1] <= W:
        dp[0][1] = 1
        dp[2][1] = 2
        if enemies[0][0] + enemies[0][1] <= W: dp[1][1] = 1
        else: dp[1][1] = 2

        dp = solution(1, dp)
        res = min(res, dp[1][N-1] + 1)
    
    if N > 1 and enemies[0][0] + enemies[0][N-1] <= W and enemies[1][0] + enemies[1][N-1] <= W:
        dp[0][1] = 0
        dp[1][1] = 1
        dp[2][1] = 1

        dp = solution(1, dp)
        res = min(res, dp[0][N-1] + 2)
    
    results.append(res)

for res in results:
    print(res)