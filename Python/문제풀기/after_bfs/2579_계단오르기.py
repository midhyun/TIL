import sys
sys.stdin = open('2579_계단오르기.txt')
input = sys.stdin.readline

n = int(input())
scores = [0]*(n+3)
dp = [0]*(n+3)
for i in range(n):
    scores[i] = int(input())
dp[0], dp[1], dp[2] = scores[0], scores[0]+scores[1], max(scores[0]+scores[2], scores[1]+scores[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + scores[i], dp[i-3]+scores[i-1]+scores[i])
print(dp[n-1])