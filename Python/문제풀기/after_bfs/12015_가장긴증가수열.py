import sys
import bisect
sys.stdin = open('12015_가장긴증가수열.txt')
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]
dp = [nums[0]]

for i in range(n):
    if nums[i] > dp[-1]:
        dp.append(nums[i])
    else:
        idx = bisect.bisect_left(dp, nums[i])
        dp[idx] = nums[i]
print(len(dp))