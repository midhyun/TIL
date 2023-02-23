import sys
input = sys.stdin.readline

N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))

dp = [0] * (N)
dp[0] = scores[0]
for i in range(1, N):
    temp = 0
    for j in range(i):
        if scores[j] < scores[i]:
            temp = max(temp, dp[j]+scores[i])
        else:
            temp = max(temp, scores[i])
    dp[i] = temp

print(max(dp))