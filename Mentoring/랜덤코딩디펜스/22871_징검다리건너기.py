import sys
sys.stdin = open('22871_징검다리건너기.txt')
input = sys.stdin.readline

def solution():
    N = int(input())
    stones = [*map(int , input().split())]
    dp = [0] + [sys.maxsize] * (N-1)

    for i in range(1, N):
        for j in range(i):
            k = max((i - j) * (1 + abs(stones[i] - stones[j])), dp[j])
            dp[i] = min(dp[i], k)
    
    print(dp[-1])

solution()