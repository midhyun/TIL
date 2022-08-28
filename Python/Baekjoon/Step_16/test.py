import sys
sys.stdin = open('9251_LCS.txt')
input = sys.stdin.readline

a = list(input().strip())
b = list(input())
dp = [[0]*1001 for _ in range(1001)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[len(a)][len(b)])