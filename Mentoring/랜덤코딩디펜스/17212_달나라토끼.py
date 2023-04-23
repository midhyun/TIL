import sys
sys.stdin = open('17212_달나라토끼.txt')
input = sys.stdin.readline
def solution():
    N = int(input())
    coins = [1, 2, 5, 7]
    min_len = max(8, N+1)
    dp = [0]*(min_len)
    dp[1], dp[2], dp[3], dp[4], dp[5], dp[6], dp[7] = 1, 1, 2, 2, 1, 2, 1
    for i in range(8, N+1):
        dp[i] = min(dp[i-1], dp[i-2], dp[i-5], dp[i-7]) + 1

    print(dp[N])

solution()