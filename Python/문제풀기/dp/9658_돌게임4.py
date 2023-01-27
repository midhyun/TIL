import sys
sys.stdin = open('9658_돌게임4.txt')
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+5)
dp[2], dp[4] = 1, 1
for i in range(5, n+1):
    if 0 in (dp[i-1], dp[i-3], dp[i-4]):
        dp[i] = 1
    else:
        dp[i] = 0

print('SK') if dp[n] else print('CY')