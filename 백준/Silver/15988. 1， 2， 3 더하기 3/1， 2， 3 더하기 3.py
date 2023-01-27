import sys
input = sys.stdin.readline

T = int(input())
nums = []
for _ in range(T):
    nums.append(int(input()))
dp = [0] * (max(nums)+5)
dp[1], dp[2], dp[3], dp[4] = 1, 2, 4, 7
for i in range(5, len(dp)):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009
for num in nums:
    print(dp[num])