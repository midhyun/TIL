import sys
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
T = int(input())

dp = [[0]*(N+1) for _ in range(3)]

for i in range(1, N):
    nums[i] += nums[i-1]

nums = [0] + nums
for i in range(1, N+1):
    start = max(0, i-T)
    dp[0][i] = max(dp[0][i-1], nums[i] - nums[start])
dp[0][0] = nums[0]

for i in range(1, 3):
    for j in range(T*(i+1), N+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-T] + (nums[j] - nums[j-T]))

print(max(dp[2]))