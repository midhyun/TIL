import sys
input = sys.stdin.readline

A = int(input())
lst = list(map(int, input().split())) # [1 4 2 3 5]
dp = [0 for _ in range(A)]
for i in range(A):
    for j in range(i):
        if lst[j] < lst[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
