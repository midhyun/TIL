import sys
sys.stdin = open('1932_정수삼각형.txt')
input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    dp.append([*map(int, input().split())])
# 인접노드는 i, i+1
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + dp[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + dp[i][j]

print(max(dp[n-1]))
