import sys
sys.stdin = open('11052_카드구매.txt')
input= sys.stdin.readline

n = int(input())
p = [0]+[*map(int, input().split())]
dp = [0]*(n+1)
for i in range(1, n+1):
    for j in range(i+1):
        dp[i] = max(dp[i], dp[i-j] + p[j])

print(dp[n])