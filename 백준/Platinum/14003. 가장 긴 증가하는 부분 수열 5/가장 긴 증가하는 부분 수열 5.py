import sys
import bisect
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]
result = [1] * n
dp = [nums[0]]

for i in range(1, n):
    if nums[i] > dp[-1]:
        dp.append(nums[i])
        result[i] = len(dp)
    else:
        idx = bisect.bisect_left(dp, nums[i])
        dp[idx] = nums[i]
        result[i] = idx + 1
        
temp = len(dp)
print(temp)
res = []
for i in range(n-1, -1, -1):
    if result[i] == temp:
        res.append(nums[i])
        temp -= 1
res.reverse()
print(*res)