import sys
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]
dp = [0]*(n)
dp[0] = nums[0]
for i in range(1, n):
    temp = 0
    for j in range(i):
        if nums[j] < nums[i]:
            temp = max(temp, dp[j])
    dp[i] = temp + nums[i]
print(max(dp))