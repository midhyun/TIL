import sys
sys.stdin = open('2302_극장좌석.txt')
input = sys.stdin.readline

N = int(input())
M = int(input())
vips = []
temp = 1
for _ in range(M):
    vip = int(input())
    vips.append(vip-temp)
    temp = vip + 1
vips.append(N-temp+1)
max_fibo = max(vips)
dp = [1]*(max_fibo+1)
for i in range(2, max_fibo+1):
    dp[i] = dp[i-1] + dp[i-2]
result = 1
for vip in vips:
    result *= dp[vip]

print(result)