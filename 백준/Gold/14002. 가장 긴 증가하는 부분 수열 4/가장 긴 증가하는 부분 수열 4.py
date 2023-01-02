import sys
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]
dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
temp = max(dp)
print(temp)
result = []
for i in range(n-1, -1, -1):
    if dp[i] == temp:
        result.append(nums[i])
        temp -= 1
result.reverse()
print(*result)