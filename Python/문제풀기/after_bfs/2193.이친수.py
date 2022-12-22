import sys
sys.stdin = open('2193.이친수.txt')
input = sys.stdin.readline

N = int(input())
dp = [0,1,1] + ([0]*N)
if N > 2:
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
print(dp[N])