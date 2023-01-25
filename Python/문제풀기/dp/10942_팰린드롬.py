import sys
sys.stdin = open('10942_팰린드롬.txt')
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]
m = int(input())
dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

for i in range(2, n):
    for j in range(n-i):
        if nums[j] == nums[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])