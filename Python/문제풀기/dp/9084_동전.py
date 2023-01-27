import sys
sys.stdin = open('9084_동전.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = [*map(int, input().split())]
    num = int(input())
    dp = [0] * (num+1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(num+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[num])