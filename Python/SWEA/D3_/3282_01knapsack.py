import sys
sys.stdin = open('3282_01knapsack.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    dp = [[0]*(k+1) for _ in range(n+1)]    # 0 kg ~ k kg 까지 1kg 늘리면서 물건도 한개씩 늘리면서
    vc = []
    for i in range(1, n+1):
        v, c = map(int, input().split())
        for k in range(1, k+1):
            if v > k:
                dp[i][k] = dp[i-1][k]
            else:
                dp[i][k] = max(dp[i-1][k-v] + c, dp[i-1][k])
    print(f'#{test_case}', dp[n][k])

## 피보나치 수열
# 1, 2, 3, 4, 5, 6
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ........
# (n-2), (n-1), n = (n-1) + (n-2)
# 재귀로 
# 
def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

fibo(1)