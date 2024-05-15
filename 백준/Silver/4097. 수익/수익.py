import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    if N == 0:
        exit()

    dp = [0]*N
    earns = []
    for i in range(N):
        earn = int(input())
        earns.append(earn)
        if dp[i-1] + earn > 0:
            dp[i] = dp[i-1] + earn
    result = max(dp)
    if result == 0:
        result = max(earns)
    print(result)

while True:
    solution()