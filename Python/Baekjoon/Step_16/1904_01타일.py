import sys
sys.stdin = open('1904_01타일.txt')
input = sys.stdin.readline


n = int(input())
dp = [1,1,2]+[0]*n
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[n])