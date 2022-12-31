import sys
import bisect
sys.stdin = open('12738_가장 긴 증가하는 부분 수열3.txt')
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]
dp = [nums[0]]

for i in range(1, n):
    if nums[i] > dp[-1]:
        dp.append(nums[i])
    else:
        idx = bisect.bisect_left(dp, nums[i])
        dp[idx] = nums[i]

print(len(dp))
print(*dp)