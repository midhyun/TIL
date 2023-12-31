import sys
sys.stdin = open('2294_동전.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [10001]*(k+1)
dp[0] = 0

for coin in coins:
    for cur in range(coin, k+1):
        dp[cur] = min(dp[cur-coin]+1, dp[cur])

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])