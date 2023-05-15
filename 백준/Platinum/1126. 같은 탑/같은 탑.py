import sys
input = sys.stdin.readline

N = int(input())
# 모든 블럭의 합이 50만을 넘지 않음,
MX = 500000
height = [0] + [*map(int, input().split())]
dp = [[0]*(MX+1) for _ in range(N+1)]
# 초기 [0][0] = 0 외의 0개의 블럭으로 차이는 존재할수 없음
for i in range(1, MX+1):
    dp[0][i] = -1

for i in range(1, N+1):
    for j in range(MX+1):
        dp[i][j] = dp[i-1][j]
        # 두 탑의 높이차이가 현재블럭보다 크고,
        # 높이차이가 j-height[i]인 경우가 존재할 때,
        if j >= height[i] and dp[i-1][j-height[i]] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-height[i]] + height[i])
        if j < height[i] and dp[i-1][height[i]-j] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][height[i]-j] + j)
        if j+height[i] <= MX:
            if dp[i-1][j+height[i]] != -1:
                dp[i][j] = max(dp[i][j], dp[i-1][j+height[i]])

print(dp[N][0] if dp[N][0] else -1)