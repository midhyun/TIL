import sys
sys.stdin = open('9465_스티커.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [[*map(int, input().split())] for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    dp[0][0], dp[1][0] = graph[0][0], graph[1][0]
    if n > 1:
        dp[1][1], dp[0][1] = dp[0][0]+graph[1][1], dp[1][0]+graph[0][1]
    for j in range(2, n):
        for i in range(2):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-2]) + graph[i][j]
    print(max(dp[0][-1], dp[1][-1]))