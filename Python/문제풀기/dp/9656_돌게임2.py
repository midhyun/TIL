import sys
sys.stdin = open('9656_돌게임2.txt')
input = sys.stdin.readline

n = int(input())
dp = [0] *(n+5)
dp[1], dp[2], dp[3] = 0, 1, 0
for i in range(4, n+1):
    if 0 in (dp[i-1], dp[i-3]):
        dp[i] = 1
    else:
        dp[i] = 0
print('SK') if dp[n] else print('CY')
