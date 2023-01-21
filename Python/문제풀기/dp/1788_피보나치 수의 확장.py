import sys
sys.stdin = open('1788_피보나치 수의 확장.txt')
input = sys.stdin.readline


n = int(input())
dp = [0] * (abs(n)+1)
if n == 0:
    print(0)
    print(0)
    exit()
elif n < 0 and abs(n) % 2 == 0:
    print(-1)
else:
    print(1)

dp[1]= 1
for i in range(2, abs(n)+1):
    dp[i] = (dp[i-1] + dp[i-2])%1000000000

print(dp[abs(n)])