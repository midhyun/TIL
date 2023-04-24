import sys
from collections import defaultdict
sys.stdin = open('21941_문자열 제거.txt')
input = sys.stdin.readline

S = input().strip()
M = int(input())
scores = defaultdict(int)
# dp[i] : i-1번째 문자열 까지의 최대 점수, 0: 0개 이므로 0점.
dp = [0] * (len(S)+1)
for i in range(2, len(S)+1):
    dp[i] = dp[i-1] + 1

for _ in range(M):
    string_a, score = input().split()
    score = int(score)
    if score > len(string_a):
        scores[string_a] = score

for i in range(len(S)):
    for k, v in scores.items():
        leng = len(k)
        if leng <= i+1 and S[i+1-leng:i+1] == k:
            dp[i+1] = max(dp[i+1-leng] + v, dp[i]+1, dp[i+1])
    else:
        dp[i+1] = max(dp[i]+1, dp[i+1])

print(dp[-1])