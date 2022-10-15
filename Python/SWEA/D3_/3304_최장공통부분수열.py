import sys
sys.stdin = open('3304_최장공통부분수열.txt')
input = sys.stdin.readline
t = int(input())
for test_case in range(1, t+1):
    a, b = input().strip().split()
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(f'#{test_case}', dp[i][j])