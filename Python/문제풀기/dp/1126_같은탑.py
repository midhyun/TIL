import sys
sys.stdin = open('1126_같은탑.txt')
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
        # 현재 블럭을 추가하지 않는 경우,
        dp[i][j] = dp[i-1][j]
        # 현재블럭을 추가해서 max값이 변하는 경우,
        if j >= height[i] and dp[i-1][j-height[i]] != -1:
            # 더 높은 탑에 height[i] 블럭 추가
            dp[i][j] = max(dp[i][j], dp[i-1][j-height[i]] + height[i])
        if j < height[i] and dp[i-1][height[i]-j] != -1:
            # 더 낮은 탑에 height[i] 블럭 추가
            dp[i][j] = max(dp[i][j], dp[i-1][height[i]-j] + j)
        # 현재블럭을 추가해도 max값이 변하지 않는 경우,
        if j+height[i] <= MX:
            if dp[i-1][j+height[i]] != -1:
                dp[i][j] = max(dp[i][j], dp[i-1][j+height[i]])

# N개의 블럭을 사용한 차이가 0일때 최대높이가 0이면
# 같은 두개의 탑을 만들 수 없으므로 -1
print(dp[N][0] if dp[N][0] else -1)