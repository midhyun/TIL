import sys
import bisect
sys.stdin = open('14003_가장 긴 증가하는 부분 수열.txt')
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]
dp = [1] * n
result = [nums[0]]

for i in range(1, n):
    if nums[i] > result[-1]:
        result.append(nums[i])
        dp[i] = dp[i-1] + 1
    else:
        idx = bisect.bisect_left(result, nums[i])
        