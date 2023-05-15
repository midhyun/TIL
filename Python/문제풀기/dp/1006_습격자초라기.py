import sys
sys.stdin = open('1006_습격자초라기.txt')
input = sys.stdin.readline

def solution(start, dp):
    for i in range(start, N):
        # i열까지 1행, 2행이 모두 채웠을 경우 최소투입소대
        # dp[1][i] + 1 = i열 2행에 소대한개 추가,
        # dp[2][i] + 1 = i열 1행에 소대한개 추가 한 것중 최소 값
        dp[0][i+1] = min(dp[1][i]+1, dp[2][i]+1)
        # i열 1행, 2행을 한개의 소대로 커버 가능한 경우
        # dp[0][i+1]의 최소값을 갱신
        if enemies[0][i] + enemies[1][i] <= W:
            dp[0][i+1] = min(dp[0][i+1], dp[0][i] + 1)
        # 1행 i-1열, i열을 한개의 소대로 커버, 2행 i-1열 i열을 한개의 소대로 커버 가능한 경우
        # dp[0][i+1]의 최소값을 갱신
        if i > 0 and enemies[0][i-1] + enemies[0][i] <= W and enemies[1][i-1] + enemies[1][i] <= W:
            dp[0][i+1] = min(dp[0][i+1], dp[0][i-1] + 2)

        if i < N-1:
            dp[1][i+1] = dp[0][i+1] + 1
            # 1행 i 와 i+1 열이 한개의 소대로 커버 가능한 경우
            if enemies[0][i] + enemies[0][i+1] <= W:
                dp[1][i+1] = min(dp[1][i+1], dp[2][i] + 1)

            dp[2][i+1] = dp[0][i+1] + 1
            # 2행 i 와 i+1 열이 한개의 소대로 커버 가능한 경우
            if enemies[1][i] + enemies[1][i+1] <= W:
                dp[2][i+1] = min(dp[2][i+1], dp[1][i] + 1)

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
    # 1행만 N-1까지 커버
    if N > 1 and enemies[0][0] + enemies[0][N-1] <= W:
        dp[0][1] = 1
        dp[1][1] = 2
        if enemies[1][0] + enemies[1][1] <= W:
            dp[2][1] = 1
        else:
            dp[2][1] = 2

        dp = solution(1, dp)
        res = min(res, dp[2][N-1] + 1)
    # 2행만 N-1까지 커버
    if N > 1 and enemies[1][0] + enemies[1][N-1] <= W:
        dp[0][1] = 1
        dp[2][1] = 2
        if enemies[0][0] + enemies[0][1] <= W:
            dp[1][1] = 1
        else:
            dp[1][1] = 2

        dp = solution(1, dp)
        res = min(res, dp[1][N-1] + 1)
    # 1,2행 모두 N-1까지 커버
    if N > 1 and enemies[0][0] + enemies[0][N-1] <= W and enemies[1][0] + enemies[1][N-1] <= W:
        dp[0][1] = 0
        dp[1][1] = 1
        dp[2][1] = 1

        dp = solution(1, dp)
        res = min(res, dp[0][N-1] + 2)
    
    results.append(res)

for res in results:
    print(res)