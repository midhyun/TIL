import sys
sys.stdin = open('1463_1로만들기.txt')
input = sys.stdin.readline

n = int(input())
dp = [0,0,1,1] +[1e6]*n*3

for i in range(2,n+1):
    if dp[i*3] > dp[i]:
        dp[i*3] = dp[i] + 1
    if dp[i*2] > dp[i]:
        dp[i*2] = dp[i] + 1
    if dp[i+1] > dp[i]:
        dp[i+1] = dp[i] + 1

print(dp[n])