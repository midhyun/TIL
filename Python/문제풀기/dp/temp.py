import sys
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]
dp = [-1000] * (n+1)
dp[0] = nums[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])
print(max(dp))