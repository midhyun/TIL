import sys
sys.stdin = open('17175_피보나치.txt')
input = sys.stdin.readline
result = 0
def fibonacci(n):
    if dp[n]:
        return dp[n]
    
    dp[n] = (fibonacci(n-1) + fibonacci(n-2) + 1) % 1000000007
    return dp[n]

N = int(input())
dp = [0] * (N+4)
dp[0], dp[1], dp[2] = 1, 1, 3
fibonacci(N)
print(dp[N])