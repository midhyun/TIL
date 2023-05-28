import sys
input = sys.stdin.readline

n = int(input())
lst = []
dp = [1]*n

for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a,b))
lst.sort()
for i in range(n):
    for j in range(i):
        if lst[i][1] > lst[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))