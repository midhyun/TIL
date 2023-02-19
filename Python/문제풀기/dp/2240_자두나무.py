import sys
sys.stdin = open('2240_자두나무.txt')
input = sys.stdin.readline

T, W = map(int, input().split())
pos = 1
dp = [[0] * (W+1) for _ in range(T)]

for i in range(T):
    x = int(input())
    if x == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
    for j in range(1, W+1):
        if j > i+1:
            break
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
        if (x == 1 and j % 2 == 0) or (x == 2 and j % 2 == 1):
            dp[i][j] += 1
for i in dp:
    print(i)
print(max(dp[-1]))