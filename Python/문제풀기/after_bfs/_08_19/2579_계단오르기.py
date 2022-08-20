import sys
sys.stdin = open('2579_계단오르기.txt')
input = sys.stdin.readline

# 2579_계단오르기
# 1) 계단은 한번에 한 계단씩, 또는 두 계단씩 오를 수 있다. 즉, 한계단을 밟으면 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 2) 연속된 세 개의 계단을 모두 밞아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 3) 마지막 도착 계단은 반드시 밟아야 한다.

steps = int(input())
scores = [int(input()) for _ in range(steps)] + [0,0,0]
dp = [0]*(steps+3)

dp[0] = scores[0]
dp[1] = scores[0] + scores [1]
dp[2] = max(scores[1] + scores[2],scores[0] + scores[2])

for i in range(3, steps):
    dp[i] = max(dp[i - 3] + scores[i - 1] + scores[i], dp[i-2] +  scores[i])
print(dp[steps-1])