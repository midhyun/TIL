import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    dp = [[0]*100001 for _ in range(6)]
    maxval = 0
    color = 0

    for i in range(N):
        a, b = map(int, input().split())
        dp[a][i] = dp[a][i-1] + 1
        if dp[a][i] == maxval:
            color = min(a, color)
        elif dp[a][i] > maxval:
            maxval = dp[a][i]
            color = a

        if a != b:
            dp[b][i] = dp[b][i-1] + 1
            if dp[b][i] == maxval:
                color = min(b, color)
            elif dp[b][i] > maxval:
                maxval = dp[b][i]
                color = b
    
    print(maxval, color)

solution()