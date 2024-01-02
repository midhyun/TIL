import sys
sys.stdin = open('15489_파스칼 삼각형.txt')
input = sys.stdin.readline

R, C, W = map(int, input().split())

n = R + W - 1
dp = [[0]*n for _ in range(n)]
# 주어진 크기만큼 1인 부분을 먼저 채움
dp[0][0] = 1
for i in range(1, n):
    dp[i][0] = 1
    dp[i][i] = 1
# 파스칼 삼각형을 만들어줌.
for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
# 주어진 꼭지점부터 숫자를 모두 더함.
res = 0
for i in range(W):
    for j in range(i+1):
        res += dp[i+R-1][j+C-1]
print(res)