import sys
sys.stdin = open('3282_01knapsack.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    dp = [[0]*(k+1) for _ in range(n+1)]
    vc = []
    for i in range(1, n+1):
        v, c = map(int, input().split())
        for k in range(1, k+1):
            if v > k:
                dp[i][k] = dp[i-1][k]
            else:
                dp[i][k] = max(dp[i-1][k-v] + c, dp[i-1][k])
    print(f'#{test_case}', dp[n][k])
