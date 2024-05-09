import sys
sys.stdin = open('4811_알약.txt')
input = sys.stdin.readline

def solution():
    N = 30
    dp = [[0]*(N+1) for _ in range(N+1)]
    
    for h in range(N+1):
        for w in range(N+1):
            if h > w: continue
            if h == 0:
                dp[w][h] = 1
            else:
                dp[w][h] = dp[w-1][h] + dp[w][h-1]
    
    while True:
        N = int(input())
        if N == 0:
            return
        print(dp[N][N])

solution()