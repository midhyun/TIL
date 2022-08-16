import sys
sys.stdin = open('24416_디피.txt')

f = {1:1, 2:1}

def fibo_dp(n):
    for i in range(3, n+1):
        cnt_dp.append(0)
        f[i] = f[i-1] + f[i-2]
    return f[n]

cnt_re = []
cnt_dp = []
n = int(input())

print(fibo_dp(n), len(cnt_dp))