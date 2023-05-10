import sys
import math
input = sys.stdin.readline

# 초기비용 H, 투자 기간 Y
H, Y = map(int, input().split())

# 1년마다 5%
# 3년마다 20%
# 5년마다 35%

dp = [0]*(Y+1)
dp[0] = H

for i in range(1, Y+1):
    if i >= 1:
        dp[i] = max(dp[i], math.floor(dp[i-1]*1.05))
    if i >= 3:
        dp[i] = max(dp[i], math.floor(dp[i-3]*1.2))
    if i >= 5:
        dp[i] = max(dp[i], math.floor(dp[i-5]*1.35))

print(dp[-1])