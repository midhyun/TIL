import sys
sys.stdin = open('20162_간식파티.txt')
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
        # j번째간식을 먹고 i번째 간식을 먹을 때
        if scores[j] < scores[i]:
            temp = max(temp, dp[j]+scores[i])
        # i번째 간식만 먹을 때
        else:
            temp = max(temp, scores[i])
    dp[i] = temp

print(scores)
print(dp)

print(max(dp))