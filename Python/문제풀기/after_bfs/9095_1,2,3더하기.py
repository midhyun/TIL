import sys
sys.stdin = open('9095_1,2,3더하기.txt')
input = sys.stdin. readline

t = int(input())
nums = [int(input()) for _ in range(t)]
dp = [0]*(max(nums)+1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, max(nums)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in range(t):
    print(dp[nums[i]])