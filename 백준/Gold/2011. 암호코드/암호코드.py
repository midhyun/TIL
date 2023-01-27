import sys
input = sys.stdin.readline

num = [*map(int, list(input().strip()))]
n = len(num)
dp = [0]*(n+1)
if num[0] == 0:
    print(0)
    exit()
dp[0], dp[1] = 1, 1
for i in range(2, n+1):
    if num[i-1] > 0:
        dp[i] += dp[i-1]
    temp = num[i-2] * 10 + num[i-1]
    if temp >= 10 and temp <= 26:
        dp[i] += dp[i-2]
    dp[i] %= 1000000
print(dp[n])