import sys
input = sys.stdin.readline
N = int(input())

dp = [0] * (N+1)
work = [[*map(int, input().split())] for _ in range(N)]

for day in range(N-1, -1, -1):
    t = work[day][0]
    if day + t <= N:
        p = work[day][1]
        dp[day] = max(dp[day+1], dp[day+t] + p)
    else:
        dp[day] = dp[day+1]

print(dp[0])