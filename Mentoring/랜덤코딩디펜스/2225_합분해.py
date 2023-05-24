import sys
sys.stdin = open('2225_합분해.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0]*(N+1) for _ in range(K+1)]
for i in range(1, N+1):
    dp[1][i] = 1
    
for i in range(2, K+1):
    for j in range(1, N+1):
        for k in range(1, j+1):
            dp[i][j] += dp[i-1][j-k]
            
print(dp)