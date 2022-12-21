import sys
sys.stdin = open('11726_2xn타일링.txt')
input = sys.stdin.readline

N = int(input())
dp = [0]*(1001)
dp[1] = 1
dp[2] = 2
if N > 2:
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
print(dp[N]%10007)