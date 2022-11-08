import sys
sys.stdin = open('12847_꿀아르바이트.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
earn = [*map(int, input().split())]
dp = [0] * (n+1)

dp[0] = sum(earn[:m])
for i in range(1,n-m+1):

    dp[i] = dp[i-1] - earn[i-1] + earn[i+m-1]

print(max(dp))