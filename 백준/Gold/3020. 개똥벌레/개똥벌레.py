import sys
input = sys.stdin.readline

def solution():
    N, H = map(int, input().split())
    dp = [0]*(H+2)
    for i in range(N):
        h = int(input())
        if i % 2 == 0:
            dp[1] += 1
            dp[h+1] -= 1
        else:
            dp[H-h+1] += 1
    for i in range(1, H+1):
        dp[i] += dp[i-1]
    dp = dp[1:H+1]
    min_value = min(dp)
    cnt = dp.count(min_value)
    print(min_value, cnt)

solution()