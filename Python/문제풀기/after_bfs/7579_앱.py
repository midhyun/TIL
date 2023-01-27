import sys
sys.stdin = open('7579_앱.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
memories = [0] + [*map(int, input().split())]
cost = [0] + [*map(int, input().split())]

INF = int(1e9)
dp = [[INF]*(m+1) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if memories[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min
        